from socket import socket
import yaml
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


host, port = (default_config.get('host'), default_config.get('port'))


try:
    sock = socket()
    sock.bind((host, port))
    sock.listen(5)

    print('server was started with {}:{}'.format(default_config.get('host'), default_config.get('port')))

    while True:
        client, address = sock.accept()
        print('client was connected with {}:{}'.format(address[0], address[1]))
        b_request = client.recv(default_config.get('buffersize'))
        print('client send message: {}'.format(b_request.decode()))
        client.send(b_request)
        client.close()

except KeyboardInterrupt:
    print('server shutdown')