from flask import Flask, jsonify, request
from flask_restful import Resource
from HRRoundPrompt import comp


class HRSkill(Resource):
    def post(self):
        prompt = '''
    I will provide you with responses to HR round questions, based on which you'll understand areas needing improvement. Can you suggest a couple of changes suitable for me?'''
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
            
