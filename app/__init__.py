import os
from flask import Flask
from flask_assets import Environment, Bundle

app = Flask(__name__)

js = Bundle("js/map.js", 
            output='gen/main.js')

assets = Environment(app)
assets.register("main.js", js)
js.build()

from app import routes