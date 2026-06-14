import os
import csv
from pathlib import Path

def find_corpus_folders(root_dir):
    """
    Находит все папки с именем 'corpus' в дереве директорий
    """
    corpus_folders = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'corpus' in dirnames:
            corpus_folders.append(Path(dirpath))
    return corpus_folders

def check_single_corpus(parent_path):
    """
    Проверяет одну пару (corpus папка + corpus.tsv)
    """
    corpus_path = parent_path / 'corpus'
    tsv_path = parent_path / 'corpus.tsv'
    
    print(f"\n📂 Проверка: {corpus_path}")
    
    # Проверка наличия TSV файла
    if not tsv_path.exists():
        print(f"   ⚠️  ПРЕДУПРЕЖДЕНИЕ: {tsv_path} не найден")
        return False
    
    # Собираем реальные файлы
    actual_files = {f.name for f in corpus_path.iterdir() if f.is_file()}
    
    # Читаем TSV
    tsv_files = set()
    try:
        with open(tsv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                if row.get('filename'):
                    tsv_files.add(row['filename'])
    except Exception as e:
        print(f"   ❌ Ошибка чтения {tsv_path}: {e}")
        return False
    
    # Сравнение
    missing_in_tsv = actual_files - tsv_files
    missing_in_fs = tsv_files - actual_files
    
    # Вывод результатов
    if not missing_in_tsv and not missing_in_fs:
        print(f"   ✅ OK: {len(actual_files)} файлов, все соответствуют")
        return True
    else:
        print(f"   ⚠️  РАСХОЖДЕНИЯ:")
        if missing_in_tsv:
            print(f"      🗑️  В папке, но нет в TSV ({len(missing_in_tsv)}):")
            for f in sorted(missing_in_tsv)[:10]:  # Показываем первые 10
                print(f"         - {f}")
            if len(missing_in_tsv) > 10:
                print(f"         ... и {len(missing_in_tsv) - 10} других")
        
        if missing_in_fs:
            print(f"      📝 В TSV, но нет в папке ({len(missing_in_fs)}):")
            for f in sorted(missing_in_fs)[:10]:
                print(f"         - {f}")
            if len(missing_in_fs) > 10:
                print(f"         ... и {len(missing_in_fs) - 10} других")
        return False

def main():
    root = "../"
    
    if not os.path.exists(root):
        print(f"Ошибка: директория {root} не существует")
        return
    
    print(f"🔍 Поиск папок 'corpus' в {root}")
    corpus_parents = find_corpus_folders(root)
    
    if not corpus_parents:
        print("Папок 'corpus' не найдено")
        return
    
    print(f"Найдено {len(corpus_parents)} папок 'corpus'")
    
    # Проверяем каждую
    results = []
    for parent in sorted(corpus_parents):
        result = check_single_corpus(parent)
        results.append(result)
    
    # Итог
    print(f"\n{'='*60}")
    print(f"ИТОГ: {sum(results)}/{len(results)} проверок пройдено успешно")
    
    if all(results):
        print("🎉 Все корпусы консистентны!")
    else:
        print("⚠️  Обнаружены расхождения в некоторых корпусах")

if __name__ == "__main__":
    main()