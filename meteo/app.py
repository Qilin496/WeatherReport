from flask import Flask
from meteo.controllers.showWeather import main

app = Flask(__name__)
app.register_blueprint(main)
app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == '__main__':
    app.run(debug=True)
