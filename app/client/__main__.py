import yaml
from socket import socket
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    required=False, help='Sets config file path'
)

args = parser.parse_args()

default_config = {'host': 'localhost',
                  'port': 8000,
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

data = input('enter data: ')

sock.send(data.encode())
print('client send data: {}'.format(data))
b_responce = sock.recv(default_config.get('buffersize'))
print(b_responce.decode())
