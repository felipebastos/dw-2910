from flask_jwt_extended import JWTManager

from typing import NoReturn
from flask import Flask

jwt = JWTManager()

def init_app(app : Flask) -> NoReturn:
    jwt.init_app(app)
