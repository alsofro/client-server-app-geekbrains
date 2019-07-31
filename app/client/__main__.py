import hashlib
import json
from argparse import ArgumentParser
from datetime import datetime as dt
from socket import socket

import yaml

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    required=False, help='Sets config file path'
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

sock = socket()
sock.connect(
    (default_config.get('host'), default_config.get('port'))
)

print('client was started')

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

s_rquest = json.dumps(request)

sock.send(s_rquest.encode())
print('client send data: {}'.format(data))
b_responce = sock.recv(default_config.get('buffersize'))
print(b_responce.decode())
