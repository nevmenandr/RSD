import os
import hashlib
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class CorpusDuplicateChecker:
    def __init__(self, root_dir, compare_method='hash'):
        """
        compare_method: 'hash' (по умолчанию) или 'content'
        'hash' - быстрее, сравнивает хеши
        'content' - медленнее, но точнее побайтовое сравнение
        """
        self.root_dir = Path(root_dir).resolve()
        self.compare_method = compare_method
        
    def get_file_hash(self, filepath, chunk_size=8192):
        """Вычисляет SHA256 хеш файла"""
        sha256_hash = hashlib.sha256()
        try:
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(chunk_size), b''):
                    sha256_hash.update(chunk)
            return sha256_hash.hexdigest()
        except Exception as e:
            print(f"      ⚠️ Ошибка чтения {filepath.name}: {e}")
            return None
    
    def files_are_equal(self, file1, file2):
        """Побайтовое сравнение двух файлов"""
        try:
            with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
                # Сравниваем блоками
                while True:
                    chunk1 = f1.read(8192)
                    chunk2 = f2.read(8192)
                    if chunk1 != chunk2:
                        return False
                    if not chunk1:
                        return True
        except Exception as e:
            print(f"      ⚠️ Ошибка сравнения: {e}")
            return False
    
    def find_duplicates_in_corpus(self, corpus_path):
        """Проверяет папку corpus на дубликаты"""
        print(f"\n📂 Проверка: {corpus_path}")
        
        # Получаем все файлы в папке (только файлы, не папки)
        all_files = [f for f in corpus_path.iterdir() if f.is_file()]
        
        if len(all_files) < 2:
            print(f"   ✅ Мало файлов для дубликатов ({len(all_files)} файл)")
            return True
        
        # Группируем по размеру
        size_groups = defaultdict(list)
        for file_path in all_files:
            size_groups[file_path.stat().st_size].append(file_path)
        
        # Проверяем только группы с одинаковым размером
        potential_duplicates = {size: files for size, files in size_groups.items() 
                                if len(files) > 1}
        
        if not potential_duplicates:
            print(f"   ✅ Дубликатов не найдено (все файлы разного размера)")
            return True
        
        # Ищем реальные дубликаты
        duplicate_groups = []
        
        for size, files in potential_duplicates.items():
            print(f"   🔍 Проверяем {len(files)} файлов размером {size:,} байт...")
            
            if self.compare_method == 'hash':
                # Метод хеширования
                hash_groups = defaultdict(list)
                for file_path in files:
                    file_hash = self.get_file_hash(file_path)
                    if file_hash:
                        hash_groups[file_hash].append(file_path)
                
                for file_hash, dup_files in hash_groups.items():
                    if len(dup_files) > 1:
                        duplicate_groups.append(dup_files)
                        
            else:  # 'content' - побайтовое сравнение
                processed = set()
                for i, file1 in enumerate(files):
                    if file1 in processed:
                        continue
                    
                    current_group = [file1]
                    for file2 in files[i+1:]:
                        if file2 not in processed and self.files_are_equal(file1, file2):
                            current_group.append(file2)
                            processed.add(file2)
                    
                    if len(current_group) > 1:
                        duplicate_groups.append(current_group)
                    processed.add(file1)
        
        # Вывод результатов
        if not duplicate_groups:
            print(f"   ✅ Дубликатов не найдено (размеры совпадают, но содержимое разное)")
            return True
        else:
            self.print_duplicates(duplicate_groups)
            return False
    
    def print_duplicates(self, duplicate_groups):
        """Выводит информацию о найденных дубликатах"""
        print(f"   ⚠️  НАЙДЕНЫ ДУБЛИКАТЫ:")
        
        total_files = 0
        for i, group in enumerate(duplicate_groups, 1):
            total_files += len(group)
            print(f"\n      Группа #{i} ({len(group)} файлов):")
            
            # Информация о первом файле
            first_file = group[0]
            stat = first_file.stat()
            print(f"         Размер: {stat.st_size:,} байт")
            print(f"         Время изменения: {datetime.fromtimestamp(stat.st_mtime)}")
            print(f"         Файлы:")
            
            for file_path in group:
                print(f"            - {file_path.name}")
                
            # Проверяем, не жесткие ли ссылки
            try:
                inodes = [f.stat().st_ino for f in group]
                if len(set(inodes)) == 1:
                    print(f"         (Примечание: это жесткие ссылки на одни и те же данные)")
            except:
                pass
        
        print(f"\n      ВСЕГО: {len(duplicate_groups)} групп, {total_files} файлов-дубликатов")
    
    def find_all_corpus_folders(self):
        """Находит все папки corpus в дереве директорий"""
        corpus_folders = []
        for dirpath, dirnames, filenames in os.walk(self.root_dir):
            if 'corpus' in dirnames:
                corpus_folders.append(Path(dirpath) / 'corpus')
        return corpus_folders
    
    def run(self):
        """Запускает проверку"""
        print(f"🔍 Поиск папок 'corpus' в {self.root_dir}")
        print(f"📌 Метод сравнения: {self.compare_method}")
        
        if not self.root_dir.exists():
            print(f"❌ Ошибка: Директория {self.root_dir} не существует")
            return
        
        corpus_folders = self.find_all_corpus_folders()
        
        if not corpus_folders:
            print("❌ Папок 'corpus' не найдено")
            return
        
        print(f"📊 Найдено {len(corpus_folders)} папок 'corpus'\n")
        
        # Проверяем каждую папку
        results = []
        for corpus_path in sorted(corpus_folders):
            result = self.find_duplicates_in_corpus(corpus_path)
            results.append(result)
        
        # Итог
        print(f"\n{'='*60}")
        print(f"ИТОГ: {sum(results)}/{len(results)} папок без дубликатов")
        
        if all(results):
            print("🎉 Отлично! Во всех папках corpus нет дубликатов!")
        else:
            print("⚠️  Внимание! Рекомендуется удалить дубликаты для экономии места")
            
            # Предлагаем действие
            print("\n💡 Для удаления дубликатов можно использовать:")
            print("   - rmlint (специализированный инструмент)")
            print("   - fdupes (простой поиск дубликатов)")
            print("   - Или дописать функцию автоматического удаления")

def main():
    # Использование с хешированием (быстрее)
    checker = CorpusDuplicateChecker("../", compare_method='hash')
    checker.run()
    
    # Для более точной проверки (медленнее) раскомментировать:
    # checker = CorpusDuplicateChecker("../", compare_method='content')
    # checker.run()

if __name__ == "__main__":
    main()