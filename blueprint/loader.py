from flask import Blueprint, render_template

loader = Blueprint("loader", __name__, template_folder='templates')