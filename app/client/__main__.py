import hashlib
import json
import zlib
from argparse import ArgumentParser
from datetime import datetime as dt
from socket import socket

import yaml

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    required=False, help='Sets config file path'
)

parser.add_argument(
    '-m', '--mode', type=str, default='r',
    required=False, help='Sets mode to client'
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


def write(sock):
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

    sock.send(b_request)
    print('client send data: {}'.format(data))


def read(sock):
    b_compressed_responce = sock.recv(default_config.get('buffersize'))
    b_responce = zlib.decompress(b_compressed_responce)

    print(b_responce.decode())


sock = socket()
sock.connect(
    (default_config.get('host'), default_config.get('port'))
)

print('client was started')

try:
    while True:
        if args.mode == 'w':
            write(sock)

        elif args.mode == 'r':
            read(sock)

except KeyboardInterrupt:
    sock.close()
    print('client was stopped')