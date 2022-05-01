import logging
from flask import Blueprint, render_template, request
from functions import search_tag

main = Blueprint('main', __name__, template_folder='templates')
logging.basicConfig(filename="info.log", level=logging.INFO)


@main.route("/")
def index_page():
    logging.info("Открыта главная страница")
    return render_template('index.html')


@main.route("/list")
def page_tag():
    logging.info("Выполнен поиск")
    get_content = request.args.get("s")
    content = search_tag(get_content)
    return render_template("post_list.html", content=content, get_content=get_content.capitalize())