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
i will provide you some answer for question which asked for counselling and based on this you have to provide suggestion for student
question-1: What are your current career interests, and how did you develop an interest in these areas?
answer-1: I am currently interested in marketing and communications. My interest developed through coursework and internships where I enjoyed creating content and analyzing its impact.

question-2: What are your key strengths and skills that you believe will be valuable in your future career?
answer-2: I believe my strengths lie in effective communication, creativity, and attention to detail. These skills are essential for success in marketing and align with my career goals.

question-3: What do you envision for your career in the next five or ten years?
answer-3: In the next five to ten years, I see myself in a leadership role within a marketing team, contributing to strategic decisions and driving innovative campaigns.

question-4: How do you see your current academic program contributing to your career goals?
answer-4: My academic program provides a strong foundation in marketing principles and allows me to explore various aspects of the field, preparing me for the challenges and opportunities in my future career.

question-5: Have you started building a professional network in your chosen field?
answer-5: Yes, I've attended industry events, connected with professionals on LinkedIn, and sought advice from mentors. Building a network is crucial for gaining insights and opening up potential opportunities.

question-6: What challenges or obstacles do you anticipate in pursuing your desired career path?
answer-6: One challenge I anticipate is the need to stay updated on evolving marketing trends. I plan to address this by engaging in continuous learning through online courses and industry publications.

question-7: Have you started researching potential employers or companies in your field of interest?
answer-7: Absolutely. I've researched several companies known for their innovative marketing strategies, and I'm particularly interested in those that value creativity and strategic thinking.

question-8: How do you plan to maintain a healthy work-life balance throughout your career?
answer-8: Maintaining work-life balance is important to me. I plan to set boundaries, prioritize self-care, and ensure that I allocate time for both personal and professional pursuits.

question-9: Are you aware of industry-specific conferences, workshops, or events that could contribute to your professional growth?
answer-9: Yes, I'm aware of upcoming marketing conferences and workshops. Attending these events will provide opportunities to learn from industry experts and stay updated on the latest trends.

question-10: How confident do you feel about your career choices, and what factors influence your confidence?
answer-10: I feel confident about my career choices because they align with my interests and strengths. Positive feedback from professors and successful internships have also contributed to my confidence.


you have to provide around 100 or less words suggestion  '''

# print(comp(PROMPT=prompt))