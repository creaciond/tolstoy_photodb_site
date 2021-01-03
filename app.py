import sqlite3

from flask import Flask
from flask import render_template, request, url_for, send_from_directory

# самописки
from db_work import search_by_title, search_by_place, search_by_rubric
from photo_desc import Photo

# конфиги
app = Flask(__name__)
app.config['FULL_FOLDER'] = "./photos/fullsize"


# сохраняем фуллсайз фотографии
@app.route("/<path:filename>")
def download_full(filename):
    return send_from_directory(app.config["FULL_FOLDER"],
                               filename, as_attachment=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download")
def download():
    return render_template("download.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/results")
def results():
    try:
        search_params = ["place", "photo_title", "rubrics"]
        if request.args:
            conn = sqlite3.connect("tolstoyphoto_db.sqlite3")
            cursor = conn.cursor()
            query_results = {}
            for param in search_params:
                query = request.args.get(param)
                if query:
                    if param == "place":
                        res = search_by_place(query, cursor)
                    elif param == "photo_title":
                        res = search_by_title(query, cursor)
                    elif param == "rubrics":
                        res = search_by_rubric(query, cursor)
                    query_results[param] = res
            cursor.close()
        overall_res = set()
        if len(query_results.keys()) > 1:
            for i, key in enumerate(query_results.keys()):
                if i == 0:
                    overall_res.update(query_results[key])
                else:
                    overall_res = overall_res & set(query_results[key])
        else:
            overall_res = query_results[next(iter(query_results))]
        if len(overall_res) > 0:
            parsed_results = [Photo(item) for item in overall_res]
            return render_template("search_results.html",
                                   photos_results=parsed_results)
        else:
            return render_template("search_empty.html")
    except sqlite3.OperationalError as e:
        print(e)
        return render_template("error.html")


if __name__ == "__main__":
    app.run()
