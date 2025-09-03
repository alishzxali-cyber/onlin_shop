from flask import Blueprint

genral = Blueprint("general", __name__)


@genral.route('/')
def main():
    return 'this is main page'

@genral.route('/about')
def about():
    return 'about us'
