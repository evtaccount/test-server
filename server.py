import os

from typing import List, Dict

from sanic import Sanic
from sanic import response

import sample_timers
import films

app = Sanic(__name__)


def _response(data: Dict = None, error: str = None):
    json = {}

    if data is not None:
        json['success'] = True
        json['data'] = data

        return response.json(json)

    if error is not None:
        json['success'] = False
        json['message'] = error

        return response.json(json)

    json['success'] = True

    return response.json(json)

@app.route("/films", methods=['GET'])
async def send_films(request):
    return _response(data=films)

@app.route("/sample_timers", methods=['GET'])
async def send_samples(request, user_id):
    return _response(data=sample_timers)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)
