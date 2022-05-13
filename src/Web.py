from flask import Flask
from typing import List

from src.web.MainController import MainController


class Web:

    @staticmethod
    def main(args: List[str]):
        app = Flask(__name__, static_url_path='/static')
        MainController.register(app)
        app.config['WTF_CSRF_ENABLED'] = False

        return app

