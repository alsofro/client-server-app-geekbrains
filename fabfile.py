from fabric.api import local


def server():
    local('python app/server')


def migrate():
    local('python server -m')


def client():
    local('python app/client')


def test():
    local('pytest --cov-report term-missing --cov app/server')


def notebook():
    local('jupyter notebook')


def kill():
    local('lsof -t -i tcp:1080 | xargs kill')
