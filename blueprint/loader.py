from flask import Blueprint, render_template

loader = Blueprint("loader", __name__, template_folder='templates')


@loader.route("/")
def get_post():
    return render_template("post_form.html")
