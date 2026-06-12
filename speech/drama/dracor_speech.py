#!/usr/bin/env python3
"""
Скрипт для загрузки и обработки пьес из корпуса rusdracor с использованием pydracor.
Требует установки: pip install pydracor
"""

import os
import shutil
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple, Optional

from pydracor import DraCorAPI

# Константы
CORPUS_NAME = "rus"
MIN_WORDS_PER_CHARACTER = 4000
CHUNK_SIZE = 2000
OUTPUT_BASE_DIR = Path("processed_plays")

def extract_character_name_from_item(item) -> Tuple[str, str]:
    """
    Извлекает русское и латинское имя персонажа из объекта API.
    Возвращает (русское_имя, латинское_имя_для_файла)
    """
    russian_name = None
    latin_name = None
    
    # Пробуем получить данные разными способами
    if hasattr(item, 'to_dict'):
        item_dict = item.to_dict()
    elif hasattr(item, '__dict__'):
        item_dict = item.__dict__
    elif isinstance(item, dict):
        item_dict = item
    else:
        # Если ничего не подходит, пробуем строковое представление
        return str(item), slugify_name(str(item))
    
    # Извлекаем имя (в TEI это может быть в разных полях)
    # Приоритет: name -> character -> id -> persName
    if 'name' in item_dict and item_dict['name']:
        russian_name = item_dict['name']
    elif 'character' in item_dict and item_dict['character']:
        russian_name = item_dict['character']
    elif 'id' in item_dict and item_dict['id']:
        russian_name = item_dict['id']
    elif 'persName' in item_dict:
        if isinstance(item_dict['persName'], dict):
            russian_name = item_dict['persName'].get('#text', str(item_dict['persName']))
        else:
            russian_name = str(item_dict['persName'])
    else:
        russian_name = str(item_dict)
    
    # Ищем латинское имя (для транслитерации)
    # В TEI оно хранится в persName с xml:lang="en" или xml:lang="de"
    if 'persName' in item_dict and isinstance(item_dict['persName'], list):
        for pers_name in item_dict['persName']:
            if isinstance(pers_name, dict):
                if pers_name.get('lang') == 'en' or pers_name.get('xml:lang') == 'en':
                    latin_name = pers_name.get('#text', '')
                    break
                elif pers_name.get('lang') == 'de' or pers_name.get('xml:lang') == 'de':
                    latin_name = pers_name.get('#text', '')
    
    # Если латинское имя не найдено, транслитерируем русское
    if not latin_name:
        latin_name = slugify_name(russian_name)
    else:
        # Очищаем латинское имя от пробелов и специальных символов
        latin_name = re.sub(r'[^a-zA-Z0-9_]', '_', latin_name)
        latin_name = re.sub(r'_+', '_', latin_name).strip('_')
    
    return russian_name, latin_name

def slugify_name(name: str) -> str:
    """
    Простая транслитерация имени персонажа (кириллица -> латиница)
    Удаляет пробелы и специальные символы.
    """
    # Словарь транслитерации
    translit_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        ' ': '_', '-': '_', 'ё': 'e'
    }
    name = name.lower().strip()
    slug = ''
    for ch in name:
        if ch in translit_map:
            slug += translit_map[ch]
        elif ch.isalpha() and ch not in translit_map:
            # Если буква не найдена в словаре (например, редкие символы)
            slug += ch
        elif ch.isdigit() or ch == '_':
            slug += ch
        # Остальные символы игнорируем
    
    # Удаляем лишние подчеркивания
    slug = re.sub(r'_+', '_', slug).strip('_')
    return slug if slug else "unknown"

def split_text_into_chunks(text: str, chunk_size: int = CHUNK_SIZE) -> List[str]:
    """Разбивает текст на куски по chunk_size слов."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def convert_to_string(text_data) -> str:
    """Преобразует текст из разных форматов в строку."""
    if isinstance(text_data, list):
        # Объединяем все элементы списка в одну строку
        return ' '.join(str(item) for item in text_data)
    elif isinstance(text_data, str):
        return text_data
    else:
        return str(text_data)

def save_chunks_for_character(play_dir: Path, character_latin_name: str, text: str, character_russian_name: str):
    """Сохраняет текст персонажа в файлы с именами latin_name_N.txt"""
    chunks = split_text_into_chunks(text)
    for idx, chunk in enumerate(chunks, start=1):
        filename = f"{character_latin_name}_{idx}.txt"
        filepath = play_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            # Добавляем комментарий с русским именем для справки
            f.write(f"# Персонаж: {character_russian_name}\n")
            f.write(f"# Кусок {idx} из {len(chunks)}\n")
            f.write("#" + "="*60 + "\n\n")
            f.write(chunk)
        print(f"    Сохранён кусок {idx} ({len(chunk.split())} слов) -> {filename}")

def process_play(play, dracor: DraCorAPI, output_base_dir: Path) -> bool:
    """Обрабатывает одну пьесу."""
    play_id = play.id
    play_name = play.name
    print(f"\nОбработка пьесы: {play_name} (ID: {play_id})")
    
    # Получаем текст по персонажам
    try:
        spoken_by_char = play.get_spoken_text_by_character()
    except Exception as e:
        print(f"  Ошибка получения текста по персонажам: {e}")
        return False
    
    # Словари для хранения данных по персонажам
    char_word_counts: Dict[str, int] = {}
    char_texts: Dict[str, str] = {}
    char_latin_names: Dict[str, str] = {}
    
    # Обрабатываем каждого персонажа
    for item in spoken_by_char:
        # Получаем русское и латинское имя
        russian_name, latin_name = extract_character_name_from_item(item)
        
        # Получаем текст
        text_data = None
        if hasattr(item, 'text'):
            text_data = item.text
        elif hasattr(item, 'get_text'):
            text_data = item.get_text()
        elif isinstance(item, dict) and 'text' in item:
            text_data = item['text']
        
        if text_data is None:
            print(f"  Предупреждение: нет текста для персонажа {russian_name}")
            continue
        
        # Преобразуем текст в строку
        text = convert_to_string(text_data)
        
        # Подсчёт слов
        words = text.split()
        word_count = len(words)
        
        char_word_counts[russian_name] = word_count
        char_texts[russian_name] = text
        char_latin_names[russian_name] = latin_name
        
        print(f"  Персонаж '{russian_name}' (латиница: {latin_name}): {word_count} слов")
    
    if not char_word_counts:
        print("  Не удалось получить данные о персонажах")
        return False
    
    # Проверяем условие: хотя бы два персонажа с >= MIN_WORDS_PER_CHARACTER слов
    qualifying_chars = [
        name for name, count in char_word_counts.items()
        if count >= MIN_WORDS_PER_CHARACTER
    ]
    
    if len(qualifying_chars) < 2:
        print(f"  Пьеса не подходит: только {len(qualifying_chars)} персонаж(ей) с ≥{MIN_WORDS_PER_CHARACTER} слов.")
        return False
    
    print(f"  Пьеса подходит! {len(qualifying_chars)} персонажей с ≥{MIN_WORDS_PER_CHARACTER} слов.")
    
    # Создаём папку для пьесы
    safe_play_name = re.sub(r'[\\/*?:"<>|]', "_", play_name)
    play_dir = output_base_dir / f"{safe_play_name}_{play_id}"
    play_dir.mkdir(parents=True, exist_ok=True)
    
    # Сохраняем метаинформацию о пьесе
    metadata_file = play_dir / "_metadata.txt"
    with open(metadata_file, 'w', encoding='utf-8') as f:
        f.write(f"Пьеса: {play_name}\n")
        f.write(f"ID: {play_id}\n")
        f.write(f"Персонажи с ≥{MIN_WORDS_PER_CHARACTER} слов:\n")
        for char_name in qualifying_chars:
            f.write(f"  - {char_name} ({char_latin_names[char_name]}): {char_word_counts[char_name]} слов\n")
    
    # Сохраняем куски для подходящих персонажей
    for char_name in qualifying_chars:
        text = char_texts[char_name]
        latin_name = char_latin_names[char_name]
        save_chunks_for_character(play_dir, latin_name, text, char_name)
    
    return True

def inspect_api_structure(dracor: DraCorAPI):
    """Отладочная функция для изучения структуры API на первой пьесе."""
    print("Изучение структуры API...")
    corpus = dracor.get_corpus(CORPUS_NAME)
    if corpus and corpus.plays:
        first_play = corpus.plays[0]
        full_play = corpus.get_play(first_play.name)
        
        print(f"\nИзучаем пьесу: {full_play.name}")
        
        # Получаем текст по персонажам
        spoken = full_play.get_spoken_text_by_character()
        print(f"\nТип результата: {type(spoken)}")
        
        if spoken:
            print(f"Количество персонажей: {len(spoken)}")
            for i, item in enumerate(spoken[:2]):  # Показываем первые 2
                print(f"\n--- Элемент {i+1} ---")
                print(f"Тип: {type(item)}")
                
                if hasattr(item, '__dict__'):
                    print(f"__dict__: {item.__dict__}")
                if hasattr(item, 'model_dump'):
                    print(f"model_dump: {item.model_dump()}")
                elif hasattr(item, 'dict'):
                    print(f"dict: {item.dict()}")
                
                # Проверяем извлечение имени
                russian, latin = extract_character_name_from_item(item)
                print(f"Извлечённое русское имя: {russian}")
                print(f"Извлечённое латинское имя: {latin}")
                
                if hasattr(item, 'text'):
                    text_preview = str(item.text)[:200] if item.text else "empty"
                    print(f"Текст (первые 200 символов): {text_preview}")

def main():
    print("Инициализация DraCor API...")
    dracor = DraCorAPI()
    
    # Раскомментируйте для отладки:
    # inspect_api_structure(dracor)
    # return
    
    print(f"Получение корпуса '{CORPUS_NAME}'...")
    corpus = dracor.get_corpus(CORPUS_NAME)
    if not corpus:
        print(f"Корпус {CORPUS_NAME} не найден.")
        return
    
    print(f"В корпусе найдено пьес: {len(corpus.plays)}")
    print("-" * 60)
    
    # Создаём итоговую папку
    if OUTPUT_BASE_DIR.exists():
        shutil.rmtree(OUTPUT_BASE_DIR)
    OUTPUT_BASE_DIR.mkdir(parents=True)
    
    processed_plays = 0
    kept_plays = 0
    
    for idx, play in enumerate(corpus.plays, 1):
        print(f"\n[{idx}/{len(corpus.plays)}] Загрузка пьесы: {play.name}")
        try:
            full_play = corpus.get_play(play.name)
        except Exception as e:
            print(f"  Ошибка загрузки пьесы {play.name}: {e}")
            continue
        
        if process_play(full_play, dracor, OUTPUT_BASE_DIR):
            kept_plays += 1
        processed_plays += 1
    
    print("\n" + "=" * 60)
    print(f"Обработано пьес: {processed_plays}")
    print(f"Пьес, соответствующих критериям (сохранены): {kept_plays}")
    print(f"Результаты сохранены в папку: {OUTPUT_BASE_DIR.absolute()}")

if __name__ == "__main__":
    main()
