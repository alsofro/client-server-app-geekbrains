from protocol import make_response
import json

def frequency_controller(request):
    data = request.get('data')
    frequency = {}
    for letter in data:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    frequency = json.dumps(frequency, ensure_ascii=False)
    return make_response(request, 200, frequency)