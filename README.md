 ![dataset](https://img.shields.io/badge/dataset-8A2BE2) ![DH](https://img.shields.io/badge/digital-humanities-blue)  ![R](https://img.shields.io/badge/r-%23276DC3.svg?style=for-the-badge&logo=r&logoColor=white) 

# Русский стилеметрический датасет

## Аннотация

В репозитории размещены русскоязычные тексты, приготовленные для стилеметрических экспериментов и учебных занятий. Все тексты находятся в общественном достоянии, сгруппированы по периодам, жанрам и объемам, имена файлов подготовлены для обработки с помощью пакета `stylo` для языка `R`. Текстовые коллекции в составе датасета подходят для проверки гипотез, тестирования инструментов автоматической классификации и организации учебных занятий по компьютерному анализу текста.

## Библиографическая ссылка

Если вы используете этот датасет в научной работе, пожалуйста, сошлитесь на него в своей публикации:

## Состав датасета

Для специалиста по истории языка и литературы очевидно, что при работе с автоматической классификацией текстов нельзя смешивать произведения и авторов разных периодов. При составлении датасета этим особенностям уделено особенное внимание.

### Тексты по авторам

#### Художественные

##### По периодам

###### XVIII в.

###### Первая половина XIX в.

###### Вторая половина XIX в.

###### Рубеж XIX-XX вв.

##### Автор vs. псевдоним

##### Тексты по переводчикам

#### Публицистические

##### По периодам

#### Научные

##### По периодам

### Тексты по жанрам

### Тексты по направлениям

#### Художественные

#### Публицистические

### Стих и проза

#### Стихотворные размеры

### Речь персонажей

#### Проза

#### Драматургия

### Сгенерированные vs. естественные

#### Модели

## Объем датасета

## Как работать с данными

### Формат представления данных

Все тексты представлены в виде отдельных файлов в формате `plain text` в кодировке `UTF-8` и имеют расширение `.txt`. Имена файлов соответствуют шаблону пакета `stylo`, позволяющему выделять на визуализации одним цветом тексты, принадлежащие к одному классу. Например, все тексты одного автора содержат имя автора до подчеркивания: `turgenev_otcy.txt`, `turgenev_rudin.txt`.

Тексты одного набора содержатся в папке с именем `corpus`, как это рекомендовано пользователям пакета `stylo`.

### Работа с помощью stylo

Самым простым способом работы с представленными здесь данными является их использование с программным пакетом `stylo` для языка `R`. Имена файлов и название папок, в которых они хранятся, соответствуют требованиям этого пакета и могут использоваться как есть без изменений. В конце [материала](https://postnauka.org/faq/99046) приведен алгоритм установки и первых шагов работы со `stylo`.

### Кластеризация и классификация текстов

Работой со `stylo` возможности этого датасета не ограничиваются. Представленные тут тексты могут использоваться для оценки (а в отдельных случаях и обучения) методов текстовой классификации.

## Сопутствующие публикации

### Обобщающие

* [Что такое стилеметрия?](https://nevmenandr.github.io/portfolio/assets/pdf/TSGI_handbook.pdf)
* [Возникновение стилеметрии](https://philclass.spbu.ru/article/view/20944)
* [К лингвистической интерпретации метода Delta Берроуза](https://www.elibrary.ru/download/elibrary_88840739_77317025.pdf)

### Стилеметрические исследования на русскоязычном материале

* [Об авторстве «Тихого Дона»](https://nevmenandr.github.io/portfolio/assets/pdf/QuietDon.pdf)
* [О переводе «Илиады» А. И. Любжина](https://nevmenandr.github.io/portfolio/assets/pdf/aristeas.pdf)
* [О прозе и переводах Набокова](https://nevmenandr.github.io/portfolio/assets/pdf/nabokov_transl.pdf)
* [Набоков и межвоенная проза](https://cyberleninka.ru/article/n/romany-vladimira-nabokova-v-kontekste-russkoy-mezhvoennoy-prozy-stilemetricheskiy-aspekt)

### Научно-популярные материалы

* [Как на самом деле определять автора с помощью компьютера?](https://habr.com/ru/articles/834912/)
* [Как вычислить существование Виктора Пелевина при помощи местоимений и предлогов](https://knife.media/club/pelevin-existence/)
* [Атрибуция текста: теория и практика](https://postnauka.org/faq/99046)

## Источники и корпуса

* [Корпус Русская классика](https://ruscorpora.ru/s/JZ83o)
* [Корпус нарративной прозы XIX в.](https://dataverse.pushdom.ru/dataset.xhtml?persistentId=doi%3A10.31860%2Fopenlit-2020.10-C004)

## Стилеметрия или стилометрия?

Термин был заимствован русским языком несколько раз. В советской традиции, которой продолжает следовать петербургская школа математической лингвистики, закрепился вариант с `е`. Московские специалисты под влиянием современного англоязычного термина `stylometry` предпочитают писать `стилометрия`. Мы выбираем первый вариант, придерживаясь курса на связность времен и поколений.

## Автор датасета

[Борис Орехов](https://nevmenandr.github.io/): 

[![Bluesky](https://img.shields.io/badge/Bluesky-0285FF?style=for-the-badge&logo=Bluesky&logoColor=white)](https://bsky.app/profile/nevmenandr.bsky.social) [![Mastodon](https://img.shields.io/badge/-MASTODON-%232B90D9?style=for-the-badge&logo=mastodon&logoColor=white)](https://mastodon.social/@nevmenandr) [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/schonenrede) [![X](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://x.com/nevmenandr) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@schonenrede/)

[![academia Logo](https://img.shields.io/badge/academia-41454A?style=flat-square&logo=academia&logoColor=white)](https://hse-ru.academia.edu/BorisOrekhov) [![arxiv Logo](https://img.shields.io/badge/-arxiv-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/search/cs?searchtype=author&query=Orekhov,+B) [![dev.to Logo](https://img.shields.io/badge/dev-000000?style=flat-square&logo=dev.to&logoColor=white)](https://dev.to/nevmenandr) [![elsevier Logo](https://img.shields.io/badge/elsevier-FF6C00?style=flat-square&logo=elsevier&logoColor=white)](https://www.scopus.com/authid/detail.uri?authorId=57190401804) [![habr Logo](https://img.shields.io/badge/habr-65A3BE?style=flat-square&logo=habr&logoColor=white)](https://habr.com/ru/users/nevmenandr/) [![huggingface Logo](https://img.shields.io/badge/huggingface-FFD21E?style=flat-square&logo=huggingface&logoColor=white)](https://huggingface.co/nevmenandr) [![orcid Logo](https://img.shields.io/badge/orcid-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0000-0002-9099-0436) [![osf Logo](https://img.shields.io/badge/osf-2CB9F1?style=flat-square&logo=osf&logoColor=white)](https://osf.io/phy74/) 

[![pypi Logo](https://img.shields.io/badge/pypi-3775A9?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/nevmenandr/) [![researchgate Logo](https://img.shields.io/badge/researchgate-00CCBB?style=flat-square&logo=researchgate&logoColor=white)](https://researchgate.net/profile/Boris-Orekhov) [![semanticscholar Logo](https://img.shields.io/badge/semanticscholar-1857B6?style=flat-square&logo=semanticscholar&logoColor=white)](https://www.semanticscholar.org/author/Boris-V.-Orekhov/2080424505)  [![wikipedia Logo](https://img.shields.io/badge/wikipedia-000000?style=flat-square&logo=wikipedia&logoColor=white)](https://ru.wikipedia.org/wiki/%D0%A3%D1%87%D0%B0%D1%81%D1%82%D0%BD%D0%B8%D0%BA:Nevmenandr)
