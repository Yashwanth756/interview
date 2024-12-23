import os
import warnings

from dotenv import load_dotenv
import google.generativeai as genai
import json
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key='AIzaSyBwYQB_87zkmivHsYX9MR9PL8Hb3y77GYE')

class GenerateQuestions:
    def __init__(self, category, level):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        generatedQuestions = self.model.generate_content(f'give me some questions and solution on {category} and {level} for preparation of interviews and give me only information in json format').text
  
        self.questions = json.loads(generatedQuestions[8:-4])
        # print(self.questions['questions'])  # Access the first 
        # print(generatedQuestions)
# GenerateQuestions('machine learning', 'hard')