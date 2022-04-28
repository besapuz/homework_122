from flask import Flask, request, render_template, send_from_directory
from blueprint.main import main
from blueprint.loader import loader
from functions import search_tag

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(loader)


@app.route("/")
def page_index():
    return main


@app.route("/list")
def page_tag():
    get_content = request.args.get("s")
    content = search_tag(get_content)
    return render_template("post_list.html", content=content, get_content=get_content)


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass
    #content = request.values.get("content")


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run(port=80)

