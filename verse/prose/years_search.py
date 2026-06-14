import re

def find_year_range(file_path):
    # Регулярное выражение для поиска годов XIX века (1800-1899)
    # Ищем числа из 4 цифр, начинающиеся с 18
    pattern = r'\b(18[0-9]{2})\b'
    
    years = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Находим все совпадения
            matches = re.findall(pattern, content)
            
            # Преобразуем строки в целые числа
            years = [int(year) for year in matches]
            
            if not years:
                print("Годы XIX века не найдены в файле.")
                return None
            
            min_year = min(years)
            max_year = max(years)
            
            # Выводим результат
            print(f"Найдено {len(years)} годов XIX века")
            print(f"Диапазон: {min_year}—{max_year}")
            print(f"Самый ранний год: {min_year}")
            print(f"Самый поздний год: {max_year}")
            
            return (min_year, max_year)
            
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

# Запуск функции
if __name__ == "__main__":
    file_path = "./corpus/verse_turgenev.txt"
    result = find_year_range(file_path)
    
    if result:
        min_year, max_year = result
        print(f"\nИтоговый диапазон: {min_year}—{max_year}")