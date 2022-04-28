from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates')


@main.route("/")
def index_page():
    return render_template('index.html')
