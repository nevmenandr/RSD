# Стихотворные тексты, сгенерированные char-based LSTM-моделями

## Состав корпуса

| Имя файла | Статус | Источник | Количество слов | Особенности генерации |
| --- | --- | --- | --- | --- |
| `gener_nekrasov_t0.1.txt` | Сгенерировано | [Модель 1](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-nekrasov) | 9502 | Температура: 0.1 |
| `gener_nekrasov_t0.3.txt` | Сгенерировано | [Модель 1](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-nekrasov) | 9687 | Температура: 0.3 |
| `gener_nekrasov_t0.5.txt` | Сгенерировано | [Модель 1](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-nekrasov) | 9450 | Температура: 0.5 |
| `gener_nekrasov_t0.7.txt` | Сгенерировано | [Модель 1](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-nekrasov) | 9257 | Температура: 0.7 |
| `gener_nekrasov_t1.txt` | Сгенерировано | [Модель 1](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-nekrasov) | 9127 | Температура: 1 |
| `gener_mandelshtam_t0.1.txt` | Сгенерировано | [Модель 2](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-mandelshtam) | 7831 | Температура: 0.1 |
| `gener_mandelshtam_t0.3.txt` | Сгенерировано | [Модель 2](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-mandelshtam) | 8577 | Температура: 0.3 |
| `gener_mandelshtam_t0.5.txt` | Сгенерировано | [Модель 2](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-mandelshtam) | 8592 | Температура: 0.5 |
| `gener_mandelshtam_t0.7.txt` | Сгенерировано | [Модель 2](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-mandelshtam) | 8603 | Температура: 0.7 |
| `gener_mandelshtam_t1.txt` | Сгенерировано | [Модель 2](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-mandelshtam) | 8610 | Температура: 1 |
| `natur_nekrasov_b1.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0010.shtml) | 9343 | N/A |
| `natur_nekrasov_b2.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0010.shtml) | 9159 | N/A |
| `natur_nekrasov_b3.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0010.shtml) | 9517 | N/A |
| `natur_nekrasov_b4.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0010.shtml) | 9527 | N/A |
| `natur_nekrasov_b5.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0010.shtml) | 9570 | N/A |
| `natur_nekrasov_b6.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0010.shtml) | 11436 | N/A |
| `natur_nekrasov_b7.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0010.shtml) | 8958 | N/A |
| `natur_nekrasov_b8.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0020.shtml) | 9919 | N/A |
| `natur_nekrasov_b9.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0020.shtml) | 9931 | N/A |
| `natur_nekrasov_b10.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0020.shtml) | 9231 | N/A |
| `natur_nekrasov_b11.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0020.shtml) | 9975 | N/A |
| `natur_nekrasov_b12.txt` | Естественного происхождения | [lib.ru](http://az.lib.ru/n/nekrasow_n_a/text_0020.shtml) | 10570 | N/A |
| `natur_mandelshtam_b1.txt` | Естественного происхождения | N/A | 12872 | N/A |
| `natur_mandelshtam_b2.txt` | Естественного происхождения | N/A | 9393 | N/A |
| `natur_mandelshtam_b3.txt` | Естественного происхождения | N/A | 9229 | N/A |
| `natur_mandelshtam_b4.txt` | Естественного происхождения | N/A | 8452 | N/A |

## Модели

1. Модель, обученная на текстах Н. Некрасова, [опубликована на Huggingface](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-nekrasov), doi: 10.57967/hf/2273; rnn_size: 512, num_layers: 3 dropout: 0.5, epoch: 50, loss: 0.9312
2. Модель, обученная на текстах О. Мандельштама, [опубликована на Huggingface](https://huggingface.co/nevmenandr/char-based-lstm-russian-poetry-mandelshtam), doi: 10.57967/hf/2272; rnn_size: 512, num_layers: 7, dropout: 0.5

## Публикации

Результаты эксперимента, поставленного с помощью текстов, порожденных использованными здесь моделями, опубликованы в препринте:  [Orekhov, Boris. ‘Identifying the Style by a Qualified Reader on a Short Fragment of Generated Poetry’. *ArXiv [Cs.CL]*, 2023. arXiv. http://arxiv.org/abs/2306.02771](https://arxiv.org/abs/2306.02771).

Пояснения к эксперименту и использованным здесь методиками и понятиям, даны в книге: *Орехов Б. В.* Электронная лира. Как и зачем искусственный интеллект пишет стихи? СПб.: Издательство Европейского университета, 2026.

## Машиночитаемая таблица с данными о корпусе

[Состав корпуса в машиночитаемом виде](corpus.tsv)

## Результаты применения Delta Берроуза

![cluster_analysis](char_lstm_CA_100_MFWs_Culled_0__Classic%20Delta__001.png)

## Файлы stylo

* [Граф расстояний](char_lstm_CA_100_MFWs_Culled_0__Classic%20Delta_EDGES.csv)
* [Таблица расстояний](distance_table_100mfw_0c.txt)
* [Список словоформ для анализа](features_analyzed_100mfw_0c.txt)
* [Частотность проанализированных словоформ по текстам](frequencies_analyzed_100mfw_0c.txt)
* [Частотность всех словоформ в текстах](table_with_frequencies.txt)
* [Список словоформ](wordlist.txt)
* [Конфигурационный файл stylo](stylo_config.txt)
