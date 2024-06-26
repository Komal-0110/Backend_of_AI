from flask_restful import Resource
from flask import request, jsonify, make_response
from model import UserModel
from flask_bcrypt import Bcrypt
from utils import createToken as token
bcrypt = Bcrypt()


class LoginUser(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        existing_user_by_email = UserModel.find_by_email(email=email)
        if existing_user_by_email:
            is_password_valid = bcrypt.check_password_hash(
                existing_user_by_email["password"], password)
            if is_password_valid:
                user_id = str(existing_user_by_email["_id"])
                res = token.encode_auth_token(user_id)
                print("res : ", user_id)
                response = make_response(jsonify({
                    "_id": user_id,
                    "username": existing_user_by_email["username"],
                    "email": existing_user_by_email["email"],
                    # "image": existing_user_by_email["image"],
                }), 201)
                response.set_cookie('Authorization', 'Bearer ' + res, httponly=True, secure=True)

                return response
            else:
                return {"message": "Invalid password"}, 401
        else:
            return {"message": "User not found"}, 404
