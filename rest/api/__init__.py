from flask import Flask, request, abort
from flask.ext.restful import Api
from flask.ext.mongoengine import MongoEngine
from config import DevConfig

api = Api()
db = MongoEngine()


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    api.init_app(app)
    return app

from controllers import *
