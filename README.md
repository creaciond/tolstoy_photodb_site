# База данных фотографий Л.Н. Толстого
Код к сайту-демо для проекта «Инстаграм Толстого» (совместно с Государственным музеем Л.Н. Толстого

## Как это устроено?
В папке `static/` — статические файлы для работы сайте:

* исходники Materialize CSS,

* картинки фавикона и фотографии-заглушки для страницы ошибки

В папке `templates/` — HTML-шаблоны страниц.

Основной код сайта — в файле `tolstoy_photodb_site.py`. Запросы к базе вынесены в `db_work.py`, в `photo_desc.py` описан класс Photo, который используется на странице выдачи поиска, чтобы при необходимости можно было быстро определить, где какая часть описания фотографии, если их нужно поменять местами (сайт ещё сырой, и будут правки со стороны музея — так будет удобнее их вносить).
