import logging
import select
import threading
from argparse import ArgumentParser
from socket import socket

import yaml

from handlers import handle_default_request


def read(sock, connections: list, b_requests_list: list, buffersize: int):
    try:
        b_request = sock.recv(buffersize)
    except:
        connections.remove(sock)
    else:
        if b_request:
            b_requests_list.append(b_request)


def write(sock, connections: list, response):
    try:
        sock.send(response)
    except:
        connections.remove(sock)


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

b_requests_list = []
connections = []

try:
    sock = socket()
    sock.bind((host, port))
    sock.settimeout(0)
    sock.listen(5)

    logging.info('server was started with {}:{}'.format(default_config.get('host'), default_config.get('port')))

    while True:
        try:
            client, address = sock.accept()

            connections.append(client)

            logging.info(
                'client was connected with {}:{} | Connections: {}'.format(address[0], address[1], connections))
        except:
            pass

        rlist, wlist, xlist = select.select(connections, connections, connections, 0)

        for r_client in rlist:
            r_thread = threading.Thread(target=read,
                                        args=(r_client, connections, b_requests_list, default_config.get('buffersize')))
            r_thread.start()

        if b_requests_list:
            b_request = b_requests_list.pop()
            b_response = handle_default_request(b_request)

            for w_client in wlist:
                w_thread = threading.Thread(target=write, args=(w_client, connections, b_response))
                w_thread.start()

except KeyboardInterrupt:
    logging.info('server shutdown')
