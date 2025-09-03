from flask import Flask
from blueprints.genral import genral

app = Flask(__name__)
app.register_blueprint(genral)

if __name__ == '__main__':
    app.run()
