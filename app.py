from flask import Flask
from flask import render_template, request, url_for

from model import *

# конфиги
app = Flask(__name__)
# БД
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tolstoyphotos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# БД и апп
db.app = app
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download")
def download():
    return render_template("download.html")


@app.route("/search")
def search():
    data_to_render = {}
    data_to_render["rubrics"] = Rubric.query.all()
    data_to_render["places"] = Location.query.all()
    data_to_render["authors"] = Author.query.all()
    return render_template("search.html", data=data_to_render)


@app.route("/photo/<photo_id>")
def photo_page(photo_id):
    photo = Photo.query.get(photo_id)
    return render_template("photo.html", photo=photo)


@app.route("/results", methods=["GET", "POST"])
def results():
    if request.form:
        print(request.form)
        query_data = {
            'author': int(request.form.get('author')) if request.form.get('author') else None,
            'location': int(request.form.get('place')) if request.form.get('place') else None,
            'photo_rubric': int(request.form.get('photo_rubric')) if request.form.get('photo_rubric') else None,
            'rubric': int(request.form.get('rubric')) if request.form.get('rubric') else None,
            'files': int(request.form.get('files')) if request.form.get('files') else None,
            'start_year': int(request.form.get('start_year')) if request.form.get('start_year') else None,
            'end_year': int(request.form.get('end_year')) if request.form.get('end_year') else None,
            'photo_title': (request.form.get('photo_title')) if request.form.get('photo_title') else None,
        }
        print(query_data)

        search_results = db.session.query(Photo) \
            .join(Author).join(Location)

# Если не введены данные поиска, то возвращаются все результаты
        if query_data['author'] == 0 and query_data['location'] == 0:
            search_results = search_results.all()
        else:
            # поиск по году-началу периода
            if query_data['start_year']:
                print(query_data['start_year'])
                res = search_results\
                    .filter(
                        query_data['start_year'] < Photo.year)
                if res:
                    search_results = res

            # поиск по году-концу периода
            if query_data['end_year']:
                print(query_data['end_year'])
                res = search_results\
                    .filter(
                        query_data['end_year'] > Photo.year)
                if res:
                    search_results = res

            # поиск по автору фотографии; если значение == 0 (не выбран автор), то пропускается
            if query_data['author'] and query_data['author'] != 0:
                print(query_data['author'])

                res = search_results\
                    .filter(
                        Photo.id_author == query_data['author'])
                if res:
                    search_results = res
                else:
                    search_results = None

            # поиск по месту, если значение == 0 (не выбрано место), то пропускается
            if query_data['location'] and query_data['location'] != 0:
                print(query_data['location'])

                res = search_results\
                    .filter(
                        Photo.id_location == query_data['location'])
                if res:
                    search_results = res
                else:
                    search_results = None
            if query_data['photo_title']:
                res = search_results\
                    .filter(
                        Photo.title == query_data['photo_title'])
                if res:
                    search_results = res
                else:
                    search_results = None
            # создание окончательного списка с результатами
            search_results = search_results.all()
        return render_template("results.html", photos_results=search_results)


if __name__ == "__main__":
    app.run()
