from pathlib import Path

from flask import render_template, redirect, request
from flask_classful import FlaskView, route  # type: ignore


class MainController(FlaskView):

    route_base = "/"

    @route('/')
    def index(self):
        with open('C:/Users/hatto/PycharmProjects/TikTokSurvivalGuide/src/static/topics/home.txt', encoding='utf8') as f:
            reader = f.readlines()

        return render_template('topic.html',
                               topic=reader)

    @route('/<id>/')
    def topic(self, id):
        path_str = '/static/topics/' + id + '.txt'
        path = str(Path(__file__).parent)
        path = path.split('\\')
        path = path[:-1]
        path = '/'.join(path)
        path += path_str

        print(path)

        with open(path, encoding='utf8') as f:
            reader = f.readlines()

        return render_template('topic.html',
                               topic=reader)


if __name__ == '__main__':
    MainController().topic('home')