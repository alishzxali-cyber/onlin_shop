from flask import Blueprint

genral = Blueprint("general", __name__)


@genral.route('/')
def hello_world():
    return 'this is main page'
