import logging
from argparse import ArgumentParser
from socket import socket

import yaml

from handlers import handle_default_request

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

host, port = (default_config.get('host'), default_config.get('port'))

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('main.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

try:
    sock = socket()
    sock.bind((host, port))
    sock.listen(5)

    logging.info('server was started with {}:{}'.format(default_config.get('host'), default_config.get('port')))

    while True:
        client, address = sock.accept()
        
        logging.info('client was connected with {}:{}'.format(address[0], address[1]))

        b_request = client.recv(default_config.get('buffersize'))
        b_responce = handle_default_request(b_request)

        client.send(b_responce)
        client.close()

except KeyboardInterrupt:
    logging.info('server shutdown')
