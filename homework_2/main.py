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


class WrongParamError(Exception):
    print('You should use "r" or "w" param!')


def csv_handler(tag='r'):
    if tag == 'r':
        pass
    if tag == 'w':
        pass
    else:
        raise WrongParamError


def json_handler(tag='r'):
    if tag == 'r':
        pass
    if tag == 'w':
        pass
    else:
        raise WrongParamError


def yaml_handler(tag='r'):
    if tag == 'r':
        pass
    if tag == 'w':
        pass
    else:
        raise WrongParamError


def csv_to_json(csv_file):
    pass


def csv_to_yaml(csv_file):
    pass


def json_to_yaml(json_file):
    pass
