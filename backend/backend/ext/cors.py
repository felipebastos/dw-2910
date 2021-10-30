from flask_cors import CORS

from typing import NoReturn
from flask import Flask

def init_app(app : Flask) -> NoReturn:
    recursos = {
        r"/api_v1/*": {"origins": "*"},
        r"/upload/*": {"origins": "*"},
        r"/api_v2/*": {"origins": "*"},
        r"/auth/*": {"origins": "*"},
     }
    cors = CORS(app, resources=recursos)
