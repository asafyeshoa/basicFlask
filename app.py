from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
# CORS(app)

flask
@app.route('/restApi', methods=['POST'])
def restApi():
    apiData = request.get_json()
    print(apiData)

    instance_id = apiData['instance_id']
    # instance_id = "i-0a4901bcad74c9faa"
    # print(instance_id)
    # period = 60
    # timeInterval = 30

    period = apiData['period']
    timeInterval = apiData['timeInterval']

    # print(instance_id)

    apiParameters = {
        'instance_id': instance_id,
        'period': period,
        'timeInterval': timeInterval
    }

    response = requests.post('https://9no2np2umh.execute-api.us-east-2.amazonaws.com/default/testFunctionForMetric',
                             json=apiParameters)

    listOfData = response.json()

    return jsonify(listOfData)


if __name__ == '__main__':
    app.run(debug=True)
