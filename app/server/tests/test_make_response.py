from datetime import datetime
from protocol import make_response


TIME = datetime.now().timestamp()

CODE = 200

REQUEST = {
    'action': 'test',
    'time': TIME,
    'data': 'message'
}


RESPONSE = {
        'action': 'test',
        'time': TIME,
        'data': 'message',
        'code': 200
    }

def test_valid_make_response():
    response = make_response(REQUEST, 200, 'message')
    assert response.get('code') == CODE