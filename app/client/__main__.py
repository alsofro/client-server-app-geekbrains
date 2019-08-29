import hashlib
import json
import logging
import threading
import zlib
from argparse import ArgumentParser
from datetime import datetime as dt
from socket import socket
from db import database_metadata, engine
import yaml

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    required=False, help='Sets config file path'
)

parser.add_argument(
    '-m', '--migrate', action='store_true'
)

args = parser.parse_args()

default_config = {'host': 'localhost',
                  'port': 1080,
                  'buffersize': 1024
                  }

if args.config:
    with open(args.config) as file:
        config = yaml.load(file, Loader=yaml.Loader)
        default_config.update(default_config)

if args.migrate:
    database_metadata.create_all(engine)

class Client:
    def __init__(self, host, port, buffersize):
        self._host = host
        self._port = port
        self._buffersize = buffersize
        self._sock = None

    def __enter__(self):
        if not self._sock:
            self._sock = socket()

    def __exit__(self, exc_type, exc_val, exc_tb):
        message = 'client shutdown'
        if exc_type:
            if not exc_type is KeyboardInterrupt:
                message = 'client stopped with error'
        logging.info(message)
        self._sock.close()
        return True

    def read(self, sock, buffersize):
        while True:
            b_compressed_responce = sock.recv(buffersize)
            b_responce = zlib.decompress(b_compressed_responce)
            print(b_responce.decode())

    def run(self):
        self._sock = socket()
        self._sock.connect((self._host, self._port))
        print('client was started')

        try:
            r_thread = threading.Thread(target=self.read, args=(self._sock, self._buffersize))
            r_thread.start()

            while True:
                hash_obj = hashlib.sha256()
                hash_obj.update(str(dt.now().timestamp()).encode())

                action = input('enter action: ')
                data = input('enter data: ')

                request = {
                    'action': action,
                    'time': dt.now().timestamp(),
                    'data': data,
                    'token': hash_obj.hexdigest()
                }

                s_request = json.dumps(request)

                b_request = zlib.compress(s_request.encode())

                self._sock.send(b_request)
                print('client send data: {}'.format(data))

        except KeyboardInterrupt:
            self._sock.close()
            print('client was stopped')


if __name__ == '__main__':
    with Client(default_config.get('host'), default_config.get('port'), default_config.get('buffersize')) as client:
        client.run()
