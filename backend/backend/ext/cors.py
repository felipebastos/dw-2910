from flask_cors import CORS

from typing import NoReturn
from flask import Flask

def init_app(app : Flask) -> NoReturn:
    cors = CORS(app, resources={r"/api_v1/*": {"origins": "*"}})
