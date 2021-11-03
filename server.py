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

        has_grouping = 'grouping' in scenario
        is_grouping = True if has_grouping is True and 'radius' in scenario['grouping'] else False

        a_star = AStar(scenario)
        result = a_star.calculate_path()
        message = result["message"]
        elapsed_time = result["elapsed_ms"]
        path = result['path']
        refined_path = result['refined_path']

        return {
            'message': message,
            'grouping': is_grouping,
            'data': {
                'elapsedMS': elapsed_time,
                'path': path,
                'refinedPath': refined_path
            }
        }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
