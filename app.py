#import logging

from flask import Flask, request, render_template, send_from_directory

from blueprint.loader import loader
from blueprint.main import main
from functions import search_tag, is_filename_allowed, add_post_json

#logging.basicConfig(filename="info.log", level=logging.INFO, format='%(asctime)s %(levelname)s:%(massages)s', encoding="utf-8")

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main)
app.register_blueprint(loader, url_prefix="/post")


@app.route("/")
def index():
    return main


@app.route("/list")
def page_tag():
    get_content = request.args.get("s")
    content = search_tag(get_content)
    return render_template("post_list.html", content=content, get_content=get_content.capitalize())


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    try:
        picture = request.files.get("picture")
        filename = picture.filename
        text_post = request.form.get('content')

    except ValueError:
        "ошибка загрузки"
    else:
        if is_filename_allowed(filename):
            path = f"../uploads/images/{filename}"
            picture.save(f"./uploads/images/{filename}")
            add_post_json(filename, text_post)
            return render_template("post_uploaded.html", picture=path, post=text_post)
        else:
            return f"Тип файла не поддерживается"


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run(port=80)
