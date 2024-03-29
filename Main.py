from flask_restful import Api
from flask import Flask, render_template
# from UserModel import User
from Registration import registration
from Login import LoginUser
from Logout import LogOutUser
from SkillAnalysis import CareerSkill
app = Flask(__name__)
api = Api(app)

# api.add_resource(User, '/users')
api.add_resource(registration, '/register')
api.add_resource(LoginUser, '/login')
api.add_resource(LogOutUser, '/logout')
api.add_resource(CareerSkill, '/career')




if __name__ == '__main__':
    app.run(port=5000)

