import os
import csv
from pathlib import Path
from collections import defaultdict, Counter

def count_words_in_file(filepath):
    """Подсчитывает количество слов в текстовом файле"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            words = text.split()
            return len(words)
    except Exception as e:
        print(f"  Ошибка чтения {filepath.name}: {e}")
        return 0

def find_all_corpus_folders(root_dir):
    """Находит все папки corpus в дереве директорий, исключая дублирующую папку combined"""
    root_path = Path(root_dir).resolve()
    corpus_folders = []
    
    # Путь к исключаемой папке (относительно корня)
    excluded_path = root_path / "author" / "nonfiction" / "science" / "combined" / "corpus"
    
    for dirpath, dirnames, filenames in os.walk(root_path):
        if 'corpus' in dirnames:
            corpus_path = Path(dirpath) / 'corpus'
            # Исключаем папку combined/corpus
            if corpus_path != excluded_path:
                corpus_folders.append(corpus_path)
    
    return corpus_folders

def find_all_tsv_files(root_dir):
    """Находит все файлы corpus.tsv в дереве директорий, исключая дублирующую папку combined"""
    root_path = Path(root_dir).resolve()
    tsv_files = []
    
    # Путь к исключаемой папке (относительно корня)
    excluded_path = root_path / "author" / "nonfiction" / "science" / "combined"
    
    for tsv_path in root_path.glob("**/corpus.tsv"):
        # Исключаем TSV-файлы из папки combined
        if excluded_path not in tsv_path.parents:
            tsv_files.append(tsv_path)
    
    return tsv_files

def extract_authors_and_years(tsv_files):
    """Извлекает авторов и годы из всех TSV-файлов"""
    authors = set()
    years = []
    
    for tsv_path in tsv_files:
        try:
            with open(tsv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    if 'author' in row and row['author']:
                        authors.add(row['author'].strip())
                    
                    if 'year' in row and row['year']:
                        try:
                            year = int(row['year'])
                            years.append(year)
                        except ValueError:
                            pass
        except Exception as e:
            print(f"Ошибка чтения {tsv_path}: {e}")
    
    return authors, years

def calculate_dataset_stats(root_dir):
    """Подсчитывает всю статистику по датасету"""
    
    print(f"**Анализ датасета:** `{root_dir}`\n")
    
    # 1. Находим все папки corpus (исключая combined)
    corpus_folders = find_all_corpus_folders(root_dir)
    
    # 2. Подсчет документов и слов
    total_documents = 0
    total_words = 0
    
    for corpus_path in corpus_folders:
        for file_path in corpus_path.iterdir():
            if file_path.is_file() and file_path.suffix == '.txt':
                total_documents += 1
                total_words += count_words_in_file(file_path)
    
    # 3. Находим все TSV-файлы (исключая combined)
    tsv_files = find_all_tsv_files(root_dir)
    authors, years = extract_authors_and_years(tsv_files)
    
    # 4. Подсчет уникальных папок с корпусами (родительские директории)
    unique_corpus_parents = len(set([p.parent for p in corpus_folders]))
    
    # 5. Вывод в виде Markdown-таблицы
    print("| Параметр | Значение |")
    print("|----------|----------|")
    print(f"| Общее число документов | {total_documents:,} |")
    print(f"| Совокупный объем слов | {total_words:,} |")
    
    if total_documents > 0:
        avg_words = total_words / total_documents
        print(f"| Средняя длина документа | {avg_words:.0f} слов |")
    
    print(f"| Общее число авторов | {len(authors):,} |")
    print(f"| Число подкорпусов | {unique_corpus_parents} |")
    
    if years:
        print(f"| Диапазон лет | {min(years)}—{max(years)} |")
        print(f"| Временной охват | {max(years) - min(years)} лет |")
    else:
        print(f"| Диапазон лет | не указан |")
    
    # Дополнительная статистика по векам
    if years:
        centuries = defaultdict(int)
        for year in years:
            century = (year - 1) // 100 + 1
            centuries[century] += 1
        
        roman_map = {18: 'XVIII', 19: 'XIX', 20: 'XX', 21: 'XXI'}
        century_str = ", ".join([f"{roman_map.get(c, c)} в. ({centuries[c]})" for c in sorted(centuries.keys())])
        print(f"| Распределение по векам | {century_str} |")
        
        # Топ-3 года
        year_counts = Counter(years)
        top_years = ", ".join([f"{y} ({year_counts[y]})" for y in sorted(year_counts.keys(), key=lambda x: year_counts[x], reverse=True)[:3]])
        print(f"| Наиболее частые годы | {top_years} |")
    
    # (Опциональная статистика по размеру корпусов закомментирована)
    
    return {
        'total_documents': total_documents,
        'total_words': total_words,
        'total_authors': len(authors),
        'year_range': (min(years), max(years)) if years else None,
        'corpus_folders': len(corpus_folders),
        'tsv_files': len(tsv_files)
    }

def main():
    root_dir = "."
    
    if not os.path.exists(root_dir):
        print(f"❌ Ошибка: Директория `{root_dir}` не существует")
        return
    
    stats = calculate_dataset_stats(root_dir)

if __name__ == "__main__":
    main()
