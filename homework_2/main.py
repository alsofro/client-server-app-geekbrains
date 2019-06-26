# Необходимые и достаточные условия

# Реализовать скрипт для чтения/записи данных в формате csv;
# Реализовать скрипт для чтения/записи данных в формате json;
# Реализовать скрипт для чтения/записи данных в формате yaml;
# Реализовать скрипт для преобразования данных в формате csv в формат json;
# Реализовать скрипт для преобразования данных в формате csv в формат yaml;
# Реализовать скрипт для преобразования данных в формате json в формат yaml.

import csv
import json

import yaml


# Exception ------------------------------------------------------------------------------

class WrongParamError(Exception):
    def __init__(self):
        super().__init__('You should use "r" or "w" param!')


# ----------------------------------------------------------------------------------------

data = [['Country', 'Capital'],
        ['Russia', 'Moscow'],
        ['USA', 'Washington'],
        ['Japan', 'Tokyo'],
        ['Switzerland', 'Bern']]


def csv_handler(tag):
    if tag == 'r':
        with open('csv_data.csv') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                print(row)
    elif tag == 'w':
        with open('csv_data.csv', 'w') as file:
            file_writer = csv.writer(file)
            for row in data:
                file_writer.writerow(row)
    else:
        raise WrongParamError


csv_handler('w')
csv_handler('r')

# ----------------------------------------------------------------------------------------

dict_to_json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
}


def json_handler(tag='r'):
    if tag == 'r':
        with open('json_data.json') as file:
            file_content = file.read()
            objs = json.loads(file_content)
        for section, commands in objs.items():
            print(section, commands)
    elif tag == 'w':
        with open('json_data.json', 'w') as file:
            json.dump(dict_to_json, file, sort_keys=True, indent=4)
    else:
        raise WrongParamError


json_handler('w')
json_handler('r')

# ----------------------------------------------------------------------------------------

action_list = ['msg_1',
               'msg_2',
               'msg_3']

to_list = ['account_1',
           'account_2',
           'account_3']

data_to_yaml = {'action': action_list, 'to': to_list}


def yaml_handler(tag='r'):
    if tag == 'r':
        with open('yaml_data.yaml') as file:
            file_content = yaml.load(file, Loader=yaml.Loader)
        print(file_content)
    elif tag == 'w':
        with open('yaml_data.yaml', 'w') as file:
            yaml.dump(data_to_yaml, file, Dumper=yaml.Dumper)
    else:
        raise WrongParamError


yaml_handler('w')
yaml_handler('r')


# ----------------------------------------------------------------------------------------

def csv_to_json():
    with open('csv_data.csv') as file:
        file_reader = csv.reader(file)
        with open('csv_to_json.json', 'w') as file:
            json.dump(dict(file_reader), file, sort_keys=True, indent=4)


csv_to_json()


# ----------------------------------------------------------------------------------------

def csv_to_yaml():
    with open('csv_data.csv') as file:
        file_reader = csv.reader(file)
        with open('csv_to_yaml.yaml', 'w') as file:
            yaml.dump(dict(file_reader), file, Dumper=yaml.Dumper)


csv_to_yaml()


# ----------------------------------------------------------------------------------------

def json_to_yaml():
    with open('json_data.json') as file:
        file_content = file.read()
        objs = json.loads(file_content)
        with open('json_to_yaml.yaml', 'w') as file:
            yaml.dump(objs, file, Dumper=yaml.Dumper)


json_to_yaml()
