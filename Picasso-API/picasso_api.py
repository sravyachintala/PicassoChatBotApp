from flask_restful import Resource, request
from flask import abort
from marshmallow import Schema, fields

from nlp_model import *
import json
from flask import jsonify, make_response

class PicassoQuerySchema(Schema):
    query = fields.Str(required=True)

picasso_api_schema = PicassoQuerySchema()

class PicassoApi(Resource):
    def get(self):
        errors = picasso_api_schema.validate(request.args)
        if errors:
            abort(400, str(errors))

        json_output = predict(request.args['query'])
        #json = predict("display Max Shipment for Albertsons/Safeway in Quarter Q3")
        response = make_response(str(json_output), 200)
        response.headers['content-type'] = 'application/json'
        return response
        