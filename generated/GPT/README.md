# Прозаические тексты, сгенерированные моделями на основе архитектуры Transformer

## Состав корпуса

| Имя файла | Статус | Источник | Количество слов | Особенности генерации |
| --- | --- | --- | --- | --- |
| `gener_chatgpt5_peasants1.txt` | Сгенерировано | ChatGPT 5 | 10267 | Промт: `Generate a short story in Russian about life in a village in the 19th century.` |
| `gener_chatgpt5_peasants2.txt` | Сгенерировано | ChatGPT 5 | 10496 | Промт: `Generate a story in Russian about life in a village in the 19th century.` |
| `gener_chatgpt5_official.txt` | Сгенерировано | ChatGPT 5 |  | Промт: `Generate a story in Russian about the life of an official in St. Petersburg in the 19th century. ` |
| `gener_aliceai_official.txt` | Сгенерировано | AliceAI |  | Промт: `Напиши художественную повесть про жизнь чиновника в Петербурге в XIX веке` |

## Машиночитаемая таблица с данными о корпусе

[Состав корпуса в машиночитаемом виде](corpus.tsv)

## Результаты применения Delta Берроуза

![cluster_analysis](GPT_CA_100_MFWs_Culled_0__Classic%20Delta__001.png)

## Файлы stylo

* [Граф расстояний](GPT_CA_100_MFWs_Culled_0__Classic%20Delta_EDGES.csv)
* [Таблица расстояний](distance_table_100mfw_0c.txt)
* [Список словоформ для анализа](features_analyzed_100mfw_0c.txt)
* [Частотность проанализированных словоформ по текстам](frequencies_analyzed_100mfw_0c.txt)
* [Частотность всех словоформ в текстах](table_with_frequencies.txt)
* [Список словоформ](wordlist.txt)
* [Конфигурационный файл stylo](stylo_config.txt)

## Публикации

[The AI Playwright: An Experiment in Literary Morphology](https://zenodo.org/records/10118816)
