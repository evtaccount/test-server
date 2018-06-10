import os

from typing import List, Dict

from sanic import Sanic
from sanic import response

# import sample_timers
# import films

app = Sanic(__name__)

films = {
    "AgfaPhoto APX 100 Professional": {
        "Rodinal": [
            {"ISO": "100", "dilution": "1+25", "developingTime": 480, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "100", "dilution": "1+50", "developingTime": 1020, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ILFORD ID-11": [
            {"ISO": "100", "dilution": "stock", "developingTime": 540, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "100", "dilution": "1+1", "developingTime": 780, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ILFORD MICROPHEN": [
            {"ISO": "100", "dilution": "stock", "developingTime": 540, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ILFORD PERCEPTOL": [
            {"ISO": "50", "dilution": "stock", "developingTime": 540, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ]
    },

    "AgfaPhoto APX 400 Professional": {
        "Rodinal": [
            {"ISO": "400", "dilution": "1+25", "developingTime": 300, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "1+50", "developingTime": 1800, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ILFORD ID-11": [
            {"ISO": "400", "dilution": "stock", "developingTime": 600, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "1:1", "developingTime": 670, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "1:3", "developingTime": 1500, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ILFORD MICROPHEN": [
            {"ISO": "400", "dilution": "stock", "developingTime": 630, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "1:1", "developingTime": 540, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "1:3", "developingTime": 1620, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ILFORD PERCEPTOL": [
            {"ISO": "320", "dilution": "stock", "developingTime": 640, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "320", "dilution": "1:1", "developingTime": 1020, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "320", "dilution": "1:3", "developingTime": 1440, "firstAgitationDuration": 60, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ]
    },

    "Arista EDU Ultra 100": {
        "ARISTA 76 POWDER": [
            {"ISO": "100", "dilution": "stock", "developinTime": 390, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "100", "dilution": "1+1", "developingTime": 540, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ARISTA PREMIUM POWDER": [
            {"ISO": "100", "dilution": "stock", "developingTime": 360, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "100", "dilution": "1+1", "developingTime": 420, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "MARATHON FILM DEVELOPER": [
            {"ISO": "100", "dilution": "1+9", "developingTime": 360, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ILFORD ID-11": [
            {"ISO": "100", "dilution": "stock", "developingTime": 390, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "100", "dilution": "1+1", "developingTime": 540, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "KODAK D-76": [
            {"ISO": "100", "dilution": "stock", "developingTime": 390, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "100", "dilution": "1+1", "developingTime": 540, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "KODAK XTOL": [
            {"ISO": "100", "dilution": "stock", "developingTime": 330, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "KODAK TMAX": [
            {"ISO": "100", "dilution": "1+4", "developingTime": 330, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "AGFA RODINAL": [
            {"ISO": "100", "dilution": "1+25", "developingTime": 210, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ]
    },

    "Arista EDU Ultra 200": {
        "ARISTA 76 POWDER": [
            {"ISO": "200", "dilution": "stock", "developingTime": 330, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "200", "dilution": "1+1", "developingTime": 510, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ARISTA PREMIUM POWDER": [
            {"ISO": "200", "dilution": "stock", "developingTime": 420, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "200", "dilution": "1+1", "DdevelopingTime": 560, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "MARATHON FILM DEVELOPER": [
            {"ISO": "200", "dilution": "1+9", "developingTime": 300, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ILFORD ID-11": [
            {"ISO": "200", "dilution": "stock", "developingTime": 330, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "200", "dilution": "1+1", "developingTime": 510, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "KODAK D-76": [
            {"ISO": "200", "dilution": "stock", "developingTime": 330, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "200", "dilution": "1+1", "developingTime": 510, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "KODAK XTOL": [
            {"ISO": "200", "dilution": "stock", "developingTime": 360, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "KODAK TMAX": [
            {"ISO": "200", "dilution": "1+4", "developingTime": 330, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "AGFA RODINAL": [
            {"ISO": "200", "dilution": "1+25", "developingTime": 300, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ]
    },

    "Arista EDU Ultra 400": {
        "ARISTA 76 POWDER": [
            {"ISO": "400", "dilution": "stock", "developingTime": 450, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "200", "dilution": "1+1", "developingTime": 750, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ARISTA PREMIUM POWDER": [
            {"ISO": "400", "dilution": "stock", "developingTime": 450, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "1+1", "developingTime": 510, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "MARATHON FILM DEVELOPER": [
            {"ISO": "400", "dilution": "1+9", "developingTime": 390, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "ILFORD ID-11": [
            {"ISO": "400", "dilution": "stock", "developingTime": 450, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "1+1", "developingTime": 750, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "KODAK D-76": [
            {"ISO": "400", "dilution": "stock", "developingTime": 450, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "1+1", "developingTime": 750, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "KODAK XTOL": [
            {"ISO": "400", "dilution": "stock", "developingTime": 420, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "KODAK TMAX": [
            {"ISO": "400", "dilution": "1+4", "developingTime": 390, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ],
        "AGFA RODINAL": [
            {"ISO": "400", "dilution": "1+25", "developingTime": 330, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ]
    },

    "Fomapan 100 Classic": {
        "Fomadon LQN": [
            {"ISO": "100", "dilution": "1+10", "developingTime": 450, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon LQR": [
            {"ISO": "100", "dilution": "1+10", "developingTime": 330, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Foma universal developer": [
            {"ISO": "100", "dilution": "stock", "developingTime": 300, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon R09": [
            {"ISO": "100", "dilution": "1+25", "developingTime": 240, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon R09": [
            {"ISO": "100", "dilution": "1+25", "developingTime": 240, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10},
            {"ISO": "100", "dilution": "1:50", "developingTime": 540, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon P": [
            {"ISO": "100", "dilution": "stock", "developingTime": 450, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon EXCEL": [
            {"ISO": "100", "dilution": "stock", "developingTime": 330, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ]
    },

    "Fomapan 200 Creative": {
        "Fomadon LQN": [
            {"ISO": "200", "dilution": "1+10", "developingTime": 330, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon LQR": [
            {"ISO": "200", "dilution": "1+10", "developingTime": 330, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Foma universal developer": [
            {"ISO": "200", "dilution": "stock", "developingTime": 210, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon R09": [
            {"ISO": "200", "dilution": "1+25", "developingTime": 300, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10},
            {"ISO": "200", "dilution": "1:50", "developingTime": 600, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon P": [
            {"ISO": "200", "dilution": "stock", "developingTime": 330, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon EXCEL": [
            {"ISO": "200", "dilution": "stock", "developingTime": 390, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ]
    },

    "Fomapan 400 Action": {
        "Fomadon LQN": [
            {"ISO": "400", "dilution": "1+10", "developingTime": 570, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon LQR": [
            {"ISO": "400", "dilution": "1+10", "developingTime": 450, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Foma universal developer": [
            {"ISO": "400", "dilution": "stock", "developingTime": 450, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon R09": [
            {"ISO": "400", "dilution": "1+25", "developingTime": 360, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10},
            {"ISO": "400", "dilution": "1:50", "developingTime": 690, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon P": [
            {"ISO": "400", "dilution": "stock", "developingTime": 630, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ],
        "Fomadon EXCEL": [
            {"ISO": "400", "dilution": "stock", "developingTime": 420, "firstAgitationDuration": 60, "periodAgitationDuration": 60, "agitationPeriod": 10}
        ]
    },

    "ILFORD DELTA 100 Professional": {
        "Kodak XTOL": [
            {"ISO": "50", "dilution": "stock", "developinTime": 405, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "50", "dilution": "1+1", "developinTime": 540, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "100", "dilution": "stock", "developinTime": 480, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "100", "dilution": "1+1", "developinTime": 630, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "200", "dilution": "stock", "developinTime": 570, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "200", "dilution": "1+1", "developinTime": 720, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "stock", "developinTime": 690, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "1+1", "developinTime": 840, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "800", "dilution": "stock", "developinTime": 870, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "800", "dilution": "1+1", "developinTime": 1005, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ]
    },

    "ILFORD DELTA 400 Professional": {
        "Kodak XTOL": [
            {"ISO": "200", "dilution": "stock", "developinTime": 360, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "200", "dilution": "1+1", "developinTime": 540, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "stock", "developinTime": 420, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "400", "dilution": "1+1", "developinTime": 630, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "800", "dilution": "stock", "developinTime": 480, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "800", "dilution": "1+1", "developinTime": 735, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "1600", "dilution": "stock", "developinTime": 600, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "1600", "dilution": "1+1", "developinTime": 870, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "3200", "dilution": "stock", "developinTime": 720, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5},
            {"ISO": "3200", "dilution": "1+1", "developinTime": 1020, "firstAgitationDuration": 30, "periodAgitationDuration": 30, "agitationPeriod": 5}
        ]
    }
}


def _response(data: films, error: str = None):
    json = {}

    json['success'] = True
    json['data'] = films

    return response.json(json)

@app.route("/films", methods=['GET'])
async def send_films(request):
    return _response(data=films)

# @app.route("/sample_timers", methods=['GET'])
# async def send_samples(request, user_id):
#     return _response(data=sample_timers)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
