import re
import os
from collections import defaultdict

def process_diary_database(sql_dump_path, output_dir):
    """
    Извлекает из SQL дампа записи дневников до 1899 года,
    группируя по авторам.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    print("Загрузка и парсинг SQL файла...")
    print("(Это может занять некоторое время для больших файлов)")
    
    # Хранилища данных
    notes = []           # (diary_id, date, text)
    diaries = {}         # diary_id -> person_id
    
    # Читаем файл целиком (если позволяет память)
    print("Чтение файла...")
    with open(sql_dump_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    print(f"Файл прочитан, размер: {len(content)} символов")
    
    # Ищем все INSERT в diary
    print("Поиск INSERT в diary...")
    # Паттерн для поиска INSERT в diary с любыми значениями
    diary_pattern = r"INSERT\s+INTO\s+`diary`\s+VALUES\s*\((.+?)\)\s*;"
    
    diary_matches = re.findall(diary_pattern, content, re.IGNORECASE | re.DOTALL)
    print(f"Найдено {len(diary_matches)} INSERT в diary")
    
    for match in diary_matches:
        # Разбираем значения
        values = parse_simple_values(match)
        # Формат: (id, person, ...)
        if len(values) >= 2:
            diary_id = values[0]
            person_id = values[1]
            if isinstance(diary_id, int) and isinstance(person_id, int):
                diaries[diary_id] = person_id
    
    print(f"Найдено связей diary->person: {len(diaries)}")
    
    # Ищем все INSERT в notes
    print("Поиск INSERT в notes...")
    notes_pattern = r"INSERT\s+INTO\s+`notes`\s+VALUES\s*\((.+?)\)\s*;"
    
    notes_matches = re.findall(notes_pattern, content, re.IGNORECASE | re.DOTALL)
    print(f"Найдено {len(notes_matches)} INSERT в notes")
    
    for match in notes_matches:
        # Разбираем значения
        values = parse_simple_values(match)
        # Формат: (id, diary, text, date_start, date_end, ...)
        if len(values) >= 4:
            diary_id = values[1] if isinstance(values[1], int) else None
            text = values[2] if isinstance(values[2], str) else None
            date = values[3] if isinstance(values[3], str) else None
            
            if diary_id and text and date and date != '0000-00-00':
                notes.append((diary_id, date, text))
    
    print(f"Найдено записей в notes: {len(notes)}")
    
    if not notes:
        print("Записи не найдены. Проверка структуры файла...")
        # Покажем первые 500 символов файла для диагностики
        print("\nПервые 500 символов файла:")
        print(content[:500])
        return
    
    # Фильтруем записи до 1899 года
    filtered_notes = []
    for diary_id, date, text in notes:
        try:
            year = int(date[:4])
            if year < 1899:
                filtered_notes.append((diary_id, date, text))
        except (ValueError, IndexError):
            pass
    
    print(f"Записей до 1899 года: {len(filtered_notes)}")
    
    if not filtered_notes:
        print("\nПримеры найденных записей (первые 10):")
        for i, (d_id, date, text) in enumerate(notes[:10]):
            print(f"  {i+1}. diary={d_id}, date={date}, text={text[:80]}...")
        return
    
    # Группируем по авторам
    author_notes = defaultdict(list)
    
    for diary_id, date, text in filtered_notes:
        person_id = diaries.get(diary_id)
        if person_id is None:
            person_id = f"diary_{diary_id}"
        
        author_notes[person_id].append({
            'diary_id': diary_id,
            'date': date,
            'text': text.strip()
        })
    
    # Сохраняем по авторам
    print(f"\nСоздание файлов для {len(author_notes)} авторов...")
    
    for person_id, notes_list in author_notes.items():
        # Сортируем по дате
        notes_list.sort(key=lambda x: x['date'])
        
        safe_name = re.sub(r'[^\w\-_\.]', '_', str(person_id))
        
        notes_filename = os.path.join(output_dir, f"person_{safe_name}_notes.txt")
        meta_filename = os.path.join(output_dir, f"person_{safe_name}_metadata.txt")
        
        years = set()
        with open(notes_filename, 'w', encoding='utf-8') as f_out:
            f_out.write(f"Person ID: {person_id}\n")
            f_out.write("-" * 50 + "\n\n")
            
            for note in notes_list:
                year = note['date'][:4]
                years.add(year)
                f_out.write(f"[{note['date']}] (Дневник ID: {note['diary_id']})\n")
                f_out.write(f"{note['text']}\n")
                f_out.write("-" * 40 + "\n\n")
        
        with open(meta_filename, 'w', encoding='utf-8') as f_meta:
            f_meta.write(f"Person ID: {person_id}\n")
            f_meta.write(f"Годы записей: {', '.join(sorted(years))}\n")
            f_meta.write(f"Количество записей: {len(notes_list)}\n")
            if notes_list:
                f_meta.write(f"Диапазон дат: {notes_list[0]['date']} - {notes_list[-1]['date']}\n")
    
    print(f"\nГотово. Создано {len(author_notes)} файлов в директории '{output_dir}'")
    
    # Выводим статистику
    all_years = set()
    for notes_list in author_notes.values():
        for note in notes_list:
            all_years.add(note['date'][:4])
    
    if all_years:
        print(f"Общий диапазон лет: {min(all_years)} - {max(all_years)}")
    
    # Покажем топ авторов
    print("\nТоп 5 авторов по количеству записей:")
    sorted_authors = sorted(author_notes.items(), key=lambda x: len(x[1]), reverse=True)[:5]
    for person_id, notes_list in sorted_authors:
        years_list = sorted(set(n['date'][:4] for n in notes_list))
        print(f"  Person {person_id}: {len(notes_list)} записей, годы: {years_list[0]}-{years_list[-1]}")


def parse_simple_values(values_str):
    """
    Упрощенный парсинг значений из SQL INSERT.
    Разбивает на значения, учитывая кавычки.
    """
    result = []
    current = ""
    in_quote = False
    escape_next = False
    
    for ch in values_str:
        if escape_next:
            current += ch
            escape_next = False
        elif ch == '\\':
            escape_next = True
        elif ch == "'" and not in_quote:
            in_quote = True
        elif ch == "'" and in_quote:
            in_quote = False
            result.append(current)
            current = ""
            continue
        elif ch == ',' and not in_quote:
            if current.strip():
                val = current.strip()
                if val == 'NULL' or val == '':
                    result.append(None)
                elif val.isdigit():
                    result.append(int(val))
                else:
                    result.append(val)
            current = ""
            continue
        else:
            current += ch
    
    # Добавляем последнее значение
    if current.strip():
        val = current.strip()
        if val == 'NULL' or val == '':
            result.append(None)
        elif val.isdigit():
            result.append(int(val))
        else:
            result.append(val)
    
    return result


if __name__ == "__main__":
    sql_file = "diary.sql"
    output_dir = "extracted_diaries"
    
    if not os.path.exists(sql_file):
        print(f"Файл {sql_file} не найден.")
        print("Укажите правильный путь к SQL дампу.")
    else:
        process_diary_database(sql_file, output_dir)
