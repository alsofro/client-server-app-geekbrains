import json
import logging

from resolvers import resolve
from protocol import (
    validate_request, make_response
)

def handle_default_request(raw_request):
    request = json.loads(raw_request.decode())

    if validate_request(request):
        action_name = request.get('action')
        controller = resolve(action_name)
        if controller:
            try:
                logging.debug('controller: {} resolved with request: {}'.format(action_name, request))
                response = controller(request)
            except Exception as err:
                logging.critical('controller: {} error: {}'.format(action_name, err))
                response = make_response(request, 500, 'internal server error')
        else:
            logging.error('controller: {} not found'.format(action_name))
            response = make_response(request, 404, 'action with name {} not supported'.format(action_name))
    else:
        logging.error('controller wrong request: {}'.format(request))
        response = make_response(request, 400, 'wrong request format')

    return json.dumps(response).encode()