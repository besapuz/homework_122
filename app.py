import logging

from flask import Flask, send_from_directory

from loader import loader
from main import main

logging.basicConfig(filename="info.log", level=logging.INFO)


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main)
app.register_blueprint(loader)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run(port=80)
