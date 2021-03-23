from flask import Flask, request #import main Flask class and request object
from flask_restful import Resource, Api
from flask_cors import CORS
from os import getenv

from picasso_api import PicassoApi

app = Flask(__name__) #create the Flask app
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(PicassoApi, '/api/v1/processquery')

if __name__ == '__main__':
    print('Starting Picasso API Server')
    app.run(debug=True, port=5000)
    