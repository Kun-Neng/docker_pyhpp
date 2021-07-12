from flask import Flask
from flask import request
from flask_cors import cross_origin

from pyhpp.a_star import AStar

app = Flask(__name__)


@app.route('/', methods=['POST'])
@cross_origin()
def path_finding():
    if request.method == 'POST':
        scenario = request.get_json()
        # print(scenario)

        a_star = AStar(scenario)
        result = a_star.calculate_path()
        message = result["message"]
        elapsed_time = result["elapsed_ms"]
        path = result['path']
        # print(path)

        return {
            'message': message,
            'data': {
                'elapsedMS': elapsed_time,
                'path': path
            }
        }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
