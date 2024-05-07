import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ.get("API_KEY")
def comp(PROMPT, MaxToken=100, outputs=1): 
    # using OpenAI's Completion module that helps execute  
    # any tasks involving text  
    response = openai.Completion.create( 
        # model name used here is text-davinci-003 
        # there are many other models available under the  
        # umbrella of GPT-3 
        model="gpt-3.5-turbo-instruct", 
        # passing the user input  
        prompt=PROMPT, 
        # generated output can have "max_tokens" number of tokens  
        max_tokens=MaxToken, 
        # number of outputs generated in one call 
        n=outputs 
    ) 
    # creating a list to store all the outputs 
    output = list() 
    for k in response['choices']: 
        output.append(k['text'].strip()) 
    return output
prompt = '''
Given the provided responses to HR round questions, identify areas for improvement and suggest changes to enhance the candidate's suitability for the role.
Question 1: Can you tell me about yourself?
Answer 1: I am a recent graduate with a degree in Business Administration. During my studies, I developed strong analytical skills and a passion for marketing. I completed internships where I gained experience in digital marketing and social media management.

Question 2: Why do you want to work for this company?
Answer 2: I admire your company's innovative approach to marketing and its commitment to community engagement. I'm excited about the opportunity to contribute my skills and grow professionally within such a dynamic organization.

Question 3: What are your strengths?
Answer 3: My strengths include effective communication, attention to detail, and problem-solving. I'm also adept at working in teams and thrive in fast-paced environments.

Question 4: What are your weaknesses?
Answer 4: I tend to be overly critical of my own work at times, which can lead to perfectionism. However, I've learned to manage this by focusing on continuous improvement and seeking feedback from colleagues.

Question 5: How do you handle pressure or stressful situations?
Answer 5: I handle pressure by prioritizing tasks, breaking them down into manageable steps, and staying organized. I also practice mindfulness techniques such as deep breathing to stay calm and focused.

Question 6: Can you describe a difficult situation you faced at work or school and how you handled it?
Answer 6: In my previous internship, we faced a tight deadline for a marketing campaign due to unexpected delays. I organized a brainstorming session with my team to generate new ideas and delegated tasks effectively to ensure we met the deadline successfully.

Question 7: Where do you see yourself in 5 years?
Answer 7: In 5 years, I envision myself as a marketing manager leading a team of talented professionals. I hope to have expanded my skills and knowledge through ongoing learning and professional development opportunities.

Question 8: Why should we hire you?
Answer 8: You should hire me because I bring a combination of relevant skills, enthusiasm, and a strong work ethic to the table. I'm confident that I can make valuable contributions to your team and help achieve the company's goals.

Question 9: Do you have any questions for us?
Answer 9: Yes, I'm curious about the company culture and opportunities for growth and advancement within the organization.

Please provide feedback on areas where the candidate can improve or make adjustments to their responses to better prepare for the HR round.
'''

