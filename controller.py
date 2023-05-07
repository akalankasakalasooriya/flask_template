from flask_restful import Resource
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

responce_header = {
    'content-type': 'application/json'
}


class Test(Resource):
    @cross_origin()
    def get(self):
        message = jsonify({"status": "ok", "success": True})
        responce_header['content-length'] = message.calculate_content_length()
        #
        res = (message, 200, responce_header)
        return res
