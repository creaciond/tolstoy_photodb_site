import sqlite3

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
    return render_template("search.html", data=data_to_render)


@app.route("/results", methods=["GET", "POST"])
def results():
    if request.form:
        search_results = db.session.query(Photo)\
            .join(Author)\
            .join(Location)\
            .join(PhotoRubric)\
            .join(Rubric)\
            .join(Files)\
            .filter(
                Photo.photo_description.like(request.form.get("photo_title")),
                Photo.id_location == request.form.get("place"),
                PhotoRubric.id_rubric == request.form.get("place")
        )
        print(search_results)
        render_template("results.html", photos_results=search_results)


if __name__ == "__main__":
    app.run()
