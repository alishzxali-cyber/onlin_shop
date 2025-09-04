from flask import Flask
from blueprints.genral import genral
from blueprints.admin import admin
from blueprints.user import user
import config
import extentions


app = Flask(__name__)
app.register_blueprint(genral)
app.register_blueprint(admin)
app.register_blueprint(user)


app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
extentions.db.init_app(app)

with app.app_context():
    extentions.db.create_all()

if __name__ == '__main__':
    app.run()