import logging
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

class HelloWorld(Resource):
    def get(self):
        logging.error('>>>>>>>>>>>>>>fail')
        return {
            'hello': 'world',
            'message': 'I am microservice on http://127.0.0.1:5000'
            }

api.add_resource(HelloWorld, '/hell')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
