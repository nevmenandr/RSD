# Прозаические тексты, сгенерированные моделями на основе архитектуры Transformer

## Состав корпуса

| Имя файла | Статус | Источник | Количество слов | Особенности генерации |
| --- | --- | --- | --- | --- |
| `gener_chatgpt5_peasants1.txt` | Сгенерировано | ChatGPT 5 | 10267 | Промпт: `Generate a short story in Russian about life in a village in the 19th century.` |
| `gener_chatgpt5_peasants2.txt` | Сгенерировано | ChatGPT 5 | 10496 | Промпт: `Generate a story in Russian about life in a village in the 19th century.` |
| `gener_chatgpt5_official.txt` | Сгенерировано | ChatGPT 5 | 5714 | Промпт: `Generate a story in Russian about the life of an official in St. Petersburg in the 19th century. ` |
| `gener_aliceai_official.txt` | Сгенерировано | [AliceAI](https://alice.yandex.ru/) | 5508 | Промпт: `Напиши художественную повесть про жизнь чиновника в Петербурге в XIX веке` |
| `gener_gigachat_official.txt` | Сгенерировано | GigaChat, gigachat_reasoning (по API) | 12780 | Промпт: `Напиши художественную повесть про жизнь чиновника в Петербурге в XIX веке` |
| `gener_gigachat_peasants.txt` | Сгенерировано | GigaChat, gigachat_reasoning (по API) | 12961 | Промпт: `Напиши художественную повесть про жизнь в деревне в XIX веке` |
| `gener_saiga_official.txt` | Сгенерировано | Saiga, IlyaGusev/saiga_yandexgpt_8b (Open Source) | 10016 | Промпт: `Напиши художественную повесть про жизнь чиновника в Петербурге в XIX веке` |
| `gener_saiga_peasants.txt` | Сгенерировано | Saiga, IlyaGusev/saiga_yandexgpt_8b (Open Source) | 8726 | Промпт: `Напиши художественную повесть про жизнь в деревне в XIX веке` |
| `gener_yandex.api_official.txt` | Сгенерировано | Yandex, yandexgpt/latest (API) | 11410 | Промпт: `Напиши художественную повесть про жизнь чиновника в Петербурге в XIX веке` |
| `gener_yandex.api_peasants.txt` | Сгенерировано | Yandex, yandexgpt/latest (API) | 14208 | Промпт: `Напиши художественную повесть про жизнь в деревне в XIX веке` |
| `natur_gogol_nos.txt` | Естественного происхождения | Н. В. Гоголь «Нос», [ilibrary.ru](https://ilibrary.ru/text/76/p.1/index.html) | 7729 | N/A |
| `natur_gogol_shinel.txt` | Естественного происхождения | Н. В. Гоголь «Шинель», [ilibrary.ru](https://ilibrary.ru/text/980/p.1/index.html) | 10144 | N/A |
| `natur_goncharov_istoriya1.txt` | Естественного происхождения | И. А. Гончаров «Обыкновенная история», [lib.ru](http://az.lib.ru/g/goncharow_i_a/text_0010.shtml) | 10008 | N/A |
| `natur_goncharov_istoriya2.txt` | Естественного происхождения | И. А. Гончаров «Обыкновенная история», [lib.ru](http://az.lib.ru/g/goncharow_i_a/text_0010.shtml) | 9009 | N/A |
| `natur_goncharov_istoriya3.txt` | Естественного происхождения | И. А. Гончаров «Обыкновенная история», [lib.ru](http://az.lib.ru/g/goncharow_i_a/text_0010.shtml) | 8720 | N/A |
| `natur_turgenev_zapiski1.txt` | Естественного происхождения | И. С. Тургенев «Хорь и Калиныч», «Ермолай и мельничиха», «Малиновая вода» [ilibrary.ru](https://ilibrary.ru/text/1204/index.html) | 9588 | N/A |
| `natur_turgenev_zapiski2.txt` | Естественного происхождения | И. С. Тургенев «Уездный лекарь», «Мой сосед Радилов», «Однодворец Овсяников» [ilibrary.ru](https://ilibrary.ru/text/1204/index.html) | 10578 | N/A |
| `natur_turgenev_zapiski3.txt` | Естественного происхождения | И. С. Тургенев «Льгов», «Бежин луг», «Касьян с Красивой Мечи» [ilibrary.ru](https://ilibrary.ru/text/1204/index.html) | 14398 | N/A |
| `natur_turgenev_zapiski4.txt` | Естественного происхождения | И. С. Тургенев «Бурмистр», «Контора», «Бирюк» [ilibrary.ru](https://ilibrary.ru/text/1204/index.html) | 10469 | N/A |


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

## Благодарности

Благодарю Дарью Гайтукиеву за помощь с созданием текстового набора.
