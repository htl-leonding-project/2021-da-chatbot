import requests
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

api = Api(app)


class Rasa(Resource):
    def get(self):
        return jsonify({"message": "Make a post request to get the result"})

    def post(self):
        id = request.get_json()['id']
        msg = request.get_json()['msg']
        url = 'http://localhost:5005/webhooks/rest/webhook'

        data = {'sender': id, 'message': msg}
        result = requests.post(url, json=data)

        print("*" * 40)
        print(result.json())
        print("*" * 40)

        return jsonify(result.json())


api.add_resource(Rasa, '/chat')

if __name__ == "__main__":
    app.run()
