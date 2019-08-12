import subprocess

from fabric.api import local


def server():
    local('python app/server')


def client():
    local('python app/client')


def multi_client(count=1):
    for i in range(int(count)):
        proc = subprocess.Popen(['cmd'], shell=True)

def test():
    local('pytest --cov-report term-missing --cov app/server')


def notebook():
    local('jupyter notebook')


def kill():
    local('lsof -t -i tcp:1080 | xargs kill')
