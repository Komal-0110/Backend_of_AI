from flask_restful import Api
from flask import Flask, render_template
# from UserModel import User
from Registration import registration
from Login import LoginUser
from Logout import LogOutUser
from SkillAnalysis import CareerSkill
from HRRoundAnalysis import HRSkill
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
CORS(app)


# api.add_resource(User, '/users')
api.add_resource(registration, '/register')
api.add_resource(LoginUser, '/login')
api.add_resource(LogOutUser, '/logout')
api.add_resource(CareerSkill, '/career')
api.add_resource(HRSkill, '/hrround')




if __name__ == '__main__':
    app.run(port=5000)

