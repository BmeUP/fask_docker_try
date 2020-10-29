from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)
req = requests

@app.route('/')
def hello_world():
    return 'Hello, World!'

class HelloWorld(Resource):
    def get(self):
        return req.get('http://172.17.0.1:5000/hell').json().get('message')

api.add_resource(HelloWorld, '/ms')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5353')