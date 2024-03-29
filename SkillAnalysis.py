from flask import Flask, jsonify, request
from flask_restful import Resource
from SkillPrompt import comp


class CareerSkill(Resource):
    def post(self):
        prompt = '''
    i will provide you some answer for question which asked for counselling and basis of my provided answers you'll understand what are my current skills, interests and capabilities. and after understanding them can you sugeest me couple of career options which are suitable for me.'''
        end = '''answer must be very short and straightforward''' 
        data= request.get_json()
        if "answers" in data:
            for answer in data["answers"]:
                prompt += answer + '\n'
            prompt += end 
            ans = comp(prompt)
            return jsonify(ans)
        else:
            return jsonify({"error": "No 'answers' key found in the request data"}), 400
            
