from flask_restful import Resource
from flask import request, jsonify, make_response


class LogOutUser(Resource):
    def post(self):
        respone = make_response(jsonify({"message": "Logged out successfully" }), 200)
        respone.set_cookie('Authentication', '', expires=0, httponly=True, secure=True)
        return respone