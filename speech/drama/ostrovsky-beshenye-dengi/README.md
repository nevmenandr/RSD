# Реплики персонажей пьесы А. Н. Островского «Бешеные деньги»

В истории русской драматургии, по всей видимости, нет пьес, в которых реплики персонажей совокупно насчитывали нужный для стилеметрического анализа объем, но в пьесе А. Н. Островского «Бешеные деньги» (1870) роли Телятева и Лидии одни из самых объемных. Тексты собраны автоматически из [Dracor](https://dracor.org/rus/ostrovsky-beshenye-dengi).

## Состав корпуса

| Имя файла  | Персонаж | Количество слов |
| --- | --- | --- |
| `telyatev_1.txt` | Телятев | 2023 |
| `telyatev_2.txt` | Телятев | 2052 |
| `lidiya_1.txt` | Лидия | 2002 |
| `lidiya_2.txt` | Лидия | 2046 |


## Машиночитаемая таблица с данными о корпусе

[Состав корпуса в машиночитаемом виде](corpus.tsv)

## Результаты применения Delta Берроуза

![cluster_analysis](ostrovsky-beshenye-dengi_CA_100_MFWs_Culled_0__Classic%20Delta__001.png)

## Файлы stylo

* [Граф расстояний](ostrovsky-beshenye-dengi_CA_100_MFWs_Culled_0__Classic%20Delta_EDGES.csv)
* [Таблица расстояний](distance_table_100mfw_0c.txt)
* [Список словоформ для анализа](features_analyzed_100mfw_0c.txt)
* [Частотность проанализированных словоформ по текстам](frequencies_analyzed_100mfw_0c.txt)
* [Частотность всех словоформ в текстах](table_with_frequencies.txt)
* [Список словоформ](wordlist.txt)
* [Конфигурационный файл stylo](stylo_config.txt)

## Код на Python, собирающий эти тексты с использованием Dracor API

[dracor_speech.py](../dracor_speech.py)

