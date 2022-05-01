import logging

from flask import Blueprint, render_template, request

from functions import is_filename_allowed, add_post_json

loader = Blueprint("loader", __name__, template_folder='templates')
logging.basicConfig(filename="info.log", level=logging.INFO)


@loader.route("/post", methods=["GET"])
def index_page():
    return render_template('post_form.html')


@loader.route("/post", methods=["POST"])
def get_post():
    picture = request.files.get("picture")
    filename = picture.filename
    text_post = request.form.get('content')
    if not picture or not text_post:
        logging.info("Данные не загружены")
        return "Ошибка загрузки"
    if is_filename_allowed(filename):
        path = f"../uploads/images/{filename}"
        picture.save(f"./uploads/images/{filename}")
        add_post_json(filename, text_post)
        return render_template("post_uploaded.html", picture=path, post=text_post)
    else:
        return f"Тип файла не поддерживается"
