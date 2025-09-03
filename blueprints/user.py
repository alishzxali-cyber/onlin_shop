from flask import Blueprint

user = Blueprint("user", __name__)


@user.route('/user')
def index():
    return 'this is user page'
