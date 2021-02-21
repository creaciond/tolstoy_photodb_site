# База данных фотографий Л.Н. Толстого
_Код к сайту для проекта «Инстаграм Толстого» (совместно с Государственным музеем Л.Н. Толстого)_

## Как это устроено?

```
tolstoy_photodb_site/
- static/
- templates/
- data/
  - miniatures/
  - fullsize/
  - kamis/
  - tei/
- app.py
- model.py
- package.json
- package-lock.json
- tolstoyphotos.db
- requirements.txt
```

|**Папка / файл**|**Что делает**|**Комментарии**|
|:---------------|:-------------|:--------------|
|`static/`|статические файлы для работы сайта: <br/> - исходники Materialize CSS,<br /> - картинки фавикона и фотографии-заглушки для страницы ошибки.||
|`templates/`|HTML-шаблоны страниц|используется фреймворк Materialize|
|`app.py`|веб-приложение||
|`model.py`|взаимодействие с БД|используется [ORM](https://habr.com/en/post/237889/) прослойка, см. [документацию модуля sqlalchemy](https://docs.sqlalchemy.org/en/13/) и [вводную статью на Хабре](https://habr.com/en/post/470285/)|
|`requirements.txt`|необходимые сторонние Python-модули||
|`package.json`, `package-lock.json`|необходимые сторонние JS-пакеты||

## Как работать?

### Установка и настройка окружения

1. Форкнуть этот репозиторий.

2. Клонировать свой форк.

3. `cd tolstoy_photodb_site`

4. `pip3 install -r requirements.txt`

5. `npm i`

6. Победа! Можно писать код :)

### Изменения и коммиты

Предлагаю считать, что `creaciond/tolstoy_photodb_site/master` — это ветка, откуда мы будем заливать сайт в интернет.

Будет круто, если изменения будут сначала в вашем форке, а потом мы будем сливать всё через пулл-реквест: хочется обезопасить себя от конфликтов, если мы будем делать несколько задач параллельно.

## Данные

### База данных

БД к сайту — `tolstoyphotos.db`, лежит на гугл-диске ([URL](https://drive.google.com/file/d/1IxFc-Z6bmeQWiCvsIz4LZWrRPDDg6XQ8/view?usp=sharing)). Чтобы всё корректно работало, её нужно положить в корень репозитория, на один уровень с `app.py`.

Схема базы есть в [wiki проекта Инстаграм Толстого](https://github.com/dhhse/tolstoy_instagram/wiki/Структура-базы-данных), здесь оставлю только картинку:

![](https://raw.githubusercontent.com/creaciond/databases_course/master/final/database_structure.png)

### Фотографии

Для корректной работы сайта нужны сами фотографии архива. Ожидаем, что они будут лежать в папке `data/`, где будут подпапки `miniatures/`, `fullsize/`, `kamis/` и `tei/`.

Скачать данные: [гугл-диск](https://drive.google.com/file/d/1Cqbqa_v5eggdoLKouxOvBW0dUwHzWRGo/view?usp=sharing). Обратите внимание: данные сжаты два раза (архив в архиве).
