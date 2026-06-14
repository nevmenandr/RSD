 ![dataset](https://img.shields.io/badge/dataset-8A2BE2) ![DH](https://img.shields.io/badge/digital-humanities-blue)  ![R](https://img.shields.io/badge/r-%23276DC3.svg?style=for-the-badge&logo=r&logoColor=white) 

# Русский стилеметрический датасет

## Аннотация

В репозитории размещены русскоязычные тексты, приготовленные для стилеметрических экспериментов и учебных занятий. Все тексты находятся в общественном достоянии, сгруппированы по периодам, жанрам и объемам, имена файлов подготовлены для обработки с помощью пакета `stylo` для языка `R`. Текстовые коллекции в составе датасета подходят для проверки гипотез, тестирования инструментов автоматической классификации и организации учебных занятий по компьютерному анализу текста.

## Библиографическая ссылка

Если вы используете этот датасет в научной работе, пожалуйста, сошлитесь на него в своей публикации:

## Состав датасета

Для специалиста по истории языка и литературы очевидно, что при работе с автоматической классификацией текстов нельзя смешивать произведения и авторов разных периодов. При составлении датасета таким разграничениям уделено особенное внимание.

### Тексты по авторам

#### Художественные

##### По периодам

###### XVIII в.

[Прозаические художественные тексты XVIII века](author/fiction/period/18/)

###### Первая половина XIX в.

[Прозаические художественные тексты первой половины XIX века](author/fiction/period/19-1/)

###### Вторая половина XIX в.

* [Небольшой набор из текстов 5 авторов для тестирования и демонстрации технологий](author/fiction/period/19-2/brevia/)
* [Большой набор из текстов 10 авторов](author/fiction/period/19-2/nonbrevia/)

###### Рубеж XIX-XX вв.

[Прозаические художественные тексты рубежа XIX-XX веков](author/fiction/period/19-20/)

##### Автор и псевдоним

##### Тексты по полу

[Прозаические художественные тексты, противопоставленные по полу автора](author/fiction/sex/)

##### Тексты по переводчикам

##### Тексты по возрасту

##### Тексты по поколению

#### Публицистические

#### Научные

[Объединенный набор для разных наук](author/nonfiction/science/combined/)

##### По отдельным наукам

* [История](author/nonfiction/science/history/)
* [Богословие](author/nonfiction/science/theology/)
* [Психофизиология](author/nonfiction/science/psychophysiology/)
* [Философия](author/nonfiction/science/philosophy/)

### Тексты по жанрам

[Тексты разных жанров](genre/)

### Тексты по направлениям

#### Художественные

#### Публицистические

[Западники и славянофилы](journalism/)

### Стих и проза

* [Стихотворные и прозаические тексты](verse/prose/)
* Стихотворные размеры

### Речь персонажей

#### Проза

#### Драматургия

* [Н. В. Гоголь «Ревизор»](speech/drama/gogol-revizor)
* [А. Н. Островский «Бешеные деньги»](speech/drama/ostrovsky-beshenye-dengi)
* [А. Н. Островский «Лес»](speech/drama/ostrovsky-les)

### Сгенерированные и естественные

* [Стихотворные тексты, сгенерированные char-based LSTM-моделями](generated/char_lstm/)
* [Прозаические тексты, сгенерированные моделями на основе архитектуры Transformer](generated/GPT/)

## Объем датасета

## Как работать с данными

### Формат представления данных

Все тексты представлены в виде отдельных файлов в формате `plain text` в кодировке `UTF-8` и имеют расширение `.txt`. Имена файлов соответствуют шаблону пакета `stylo`, позволяющему выделять на визуализации одним цветом тексты, принадлежащие к одному классу. Например, все тексты одного автора содержат имя автора до подчеркивания: `turgenev_otcy.txt`, `turgenev_nakanune.txt`.

Тексты одного набора содержатся в папке с именем `corpus`, как это рекомендовано пользователям пакета `stylo`. К каждому набору приложен файл `README.md`, раскрывающий закодированные в имени файла имя автора (или другой идентификатор класса) и название текста и в отдельных случаях источник текста.

### Работа с помощью stylo

Самым простым способом работы с представленными здесь данными является их использование с программным пакетом `stylo` для языка `R`. Имена файлов и название папок, в которых они хранятся, соответствуют требованиям этого пакета и могут использоваться как есть без изменений. В конце [материала](https://postnauka.org/faq/99046) приведен алгоритм установки и первых шагов работы со `stylo`.

#### Загрузка и первичный анализ с `stylo` (R)

```r
library(stylo)

# Укажите путь к папке (например, с текстами авторов XIX в.)
setwd("RSD/author/fiction/period/19-2/nonbrevia/")

# Запуск стилеметрического анализа
stylo()
```

### Кластеризация и классификация текстов

Работой со `stylo` возможности этого датасета не ограничиваются. Представленные тут тексты могут использоваться для оценки (а в отдельных случаях и обучения) методов текстовой классификации и кластеризации.

```python
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE
from scipy.cluster.hierarchy import dendrogram, linkage

# Загрузка
path = "RSD/author/fiction/period/19-2/nonbrevia/corpus/"
texts, names = zip(*[(f.read_text(encoding='utf-8'), f.stem) for f in Path(path).glob("*.txt")])

# Векторизация
X = TfidfVectorizer(max_features=500).fit_transform(texts).toarray()

# Визуализация
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
tsne = TSNE(n_components=2, random_state=42).fit_transform(X)
ax1.scatter(tsne[:, 0], tsne[:, 1], s=100)
for i, n in enumerate(names): ax1.annotate(n, tsne[i], fontsize=8)
ax1.set_title("t-SNE")

dendrogram(linkage(X, method='ward'), labels=names, ax=ax2, leaf_rotation=90)
ax2.set_title("Дендрограмма")
plt.tight_layout()
plt.savefig('clusters.png', dpi=150)
plt.show()
```

### Тесты

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](tests/)

Датасет содержит [тесты](tests/) для проверки консистентности данных и отсутствия дубликатов.

## Сопутствующие публикации

### Обобщающие

* [Что такое стилеметрия?](https://nevmenandr.github.io/portfolio/assets/pdf/TSGI_handbook.pdf)
* [Возникновение стилеметрии](https://philclass.spbu.ru/article/view/20944)
* [К лингвистической интерпретации метода Delta Берроуза](https://www.elibrary.ru/download/elibrary_88840739_77317025.pdf)

### Стилеметрические исследования на русскоязычном материале

* [Об авторстве «Тихого Дона»](https://nevmenandr.github.io/portfolio/assets/pdf/QuietDon.pdf)
* [О переводе «Илиады» А. И. Любжина](https://nevmenandr.github.io/portfolio/assets/pdf/aristeas.pdf)
* [О прозе и переводах В. В. Набокова](https://nevmenandr.github.io/portfolio/assets/pdf/nabokov_transl.pdf)
* [В. В. Набоков и межвоенная проза](https://cyberleninka.ru/article/n/romany-vladimira-nabokova-v-kontekste-russkoy-mezhvoennoy-prozy-stilemetricheskiy-aspekt)

### Научно-популярные материалы

* [Как на самом деле определять автора с помощью компьютера?](https://habr.com/ru/articles/834912/)
* [Как вычислить существование Виктора Пелевина при помощи местоимений и предлогов](https://knife.media/club/pelevin-existence/)
* [Атрибуция текста: теория и практика](https://postnauka.org/faq/99046)

## Источники и корпуса

* [Корпус Русская классика](https://ruscorpora.ru/s/JZ83o)
* [Корпус нарративной прозы XIX в.](https://dataverse.pushdom.ru/dataset.xhtml?persistentId=doi%3A10.31860%2Fopenlit-2020.10-C004)
* [Код и данные для статьи на Хабре про атрибуцию](https://github.com/nevmenandr/delta_illustr/)
* [Поэтический корпус русского языка](https://github.com/IlyaGusev/PoetryCorpus)
* [Русский драматический корпус](https://dracor.org/rus)

## Стилеметрия или стилометрия?

Термин был заимствован русским языком несколько раз. В советской традиции, которой продолжает следовать петербургская школа математической лингвистики, закрепился вариант с `е`. Московские специалисты под влиянием современного англоязычного термина `stylometry` предпочитают писать `стилометрия`. Мы выбираем первый вариант, придерживаясь курса на связность времен и поколений.

## Лицензия

Тексты произведений находятся в общественном достоянии (public domain) в соответствии с законодательством РФ.

Метаданные, структура датасета и вспомогательные скрипты распространяются под лицензией [GPL-3.0 license](LICENSE) — вы можете использовать, адаптировать и распространять их при условии указания авторства и сохранения тех же условий.

## Если вы нашли ошибку или хотите добавить тексты

1. Откройте [Issue](https://github.com/nevmenandr/RSD/issues/new) на GitHub
2. Пришлите Pull Request с исправлением
3. Или напишите автору: nevmenandr@gmail.com

При добавлении новых текстов убедитесь, что:
- Текст находится в общественном достоянии
- Соблюден формат именования `author_title.txt`
- Файл добавлен в соответствующую папку `corpus`
- Обновлен `README.md` и `corpus.tsv`

## Часто задаваемые вопросы

**Вопрос:** Могу ли я использовать датасет для коммерческих проектов?
**Ответ:** Да, тексты находятся в public domain. Метаданные — под CC BY-SA 3.0.

**Вопрос:** Как добавить свой собственный текст в датасет для эксперимента?
**Ответ:** Положите файл в нужную папку `corpus`, соблюдая именование `автор_название.txt`.

**Вопрос:** Поддерживаются ли другие языки, кроме русского?
**Ответ:** Нет, это специализированный русскоязычный датасет.

## Автор датасета

[Борис Орехов](https://nevmenandr.github.io/): 

[![Bluesky](https://img.shields.io/badge/Bluesky-0285FF?style=for-the-badge&logo=Bluesky&logoColor=white)](https://bsky.app/profile/nevmenandr.bsky.social) [![Mastodon](https://img.shields.io/badge/-MASTODON-%232B90D9?style=for-the-badge&logo=mastodon&logoColor=white)](https://mastodon.social/@nevmenandr) [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/schonenrede) [![X](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://x.com/nevmenandr) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@schonenrede/)

[![academia Logo](https://img.shields.io/badge/academia-41454A?style=flat-square&logo=academia&logoColor=white)](https://hse-ru.academia.edu/BorisOrekhov) [![arxiv Logo](https://img.shields.io/badge/-arxiv-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/search/cs?searchtype=author&query=Orekhov,+B) [![dev.to Logo](https://img.shields.io/badge/dev-000000?style=flat-square&logo=dev.to&logoColor=white)](https://dev.to/nevmenandr) [![elsevier Logo](https://img.shields.io/badge/elsevier-FF6C00?style=flat-square&logo=elsevier&logoColor=white)](https://www.scopus.com/authid/detail.uri?authorId=57190401804) [![habr Logo](https://img.shields.io/badge/habr-65A3BE?style=flat-square&logo=habr&logoColor=white)](https://habr.com/ru/users/nevmenandr/) [![huggingface Logo](https://img.shields.io/badge/huggingface-FFD21E?style=flat-square&logo=huggingface&logoColor=white)](https://huggingface.co/nevmenandr) [![orcid Logo](https://img.shields.io/badge/orcid-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0000-0002-9099-0436) [![osf Logo](https://img.shields.io/badge/osf-2CB9F1?style=flat-square&logo=osf&logoColor=white)](https://osf.io/phy74/) 

[![pypi Logo](https://img.shields.io/badge/pypi-3775A9?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/nevmenandr/) [![researchgate Logo](https://img.shields.io/badge/researchgate-00CCBB?style=flat-square&logo=researchgate&logoColor=white)](https://researchgate.net/profile/Boris-Orekhov) [![semanticscholar Logo](https://img.shields.io/badge/semanticscholar-1857B6?style=flat-square&logo=semanticscholar&logoColor=white)](https://www.semanticscholar.org/author/Boris-V.-Orekhov/2080424505)  [![wikipedia Logo](https://img.shields.io/badge/wikipedia-000000?style=flat-square&logo=wikipedia&logoColor=white)](https://ru.wikipedia.org/wiki/%D0%A3%D1%87%D0%B0%D1%81%D1%82%D0%BD%D0%B8%D0%BA:Nevmenandr)
