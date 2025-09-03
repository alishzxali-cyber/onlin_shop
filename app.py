from flask import Flask
from blueprints.genral import genral
from blueprints.admin import  admin
from blueprints.user import  user


app = Flask(__name__)
app.register_blueprint(genral)
app.register_blueprint(admin)
app.register_blueprint(user)


if __name__ == '__main__':
    app.run()
