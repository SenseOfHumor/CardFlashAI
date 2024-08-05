import numpy as np
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()



#configure the API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-1.0-pro')

## creating a history of the tasks, user query, and the response
history = '''

'''



def askGemini(document):
    global reply
    global history
    # template AKA system prompt
    template = '''
    You will act as an expert in making flash cards for students. You will be given a document and a user prompt.
    You will have to generate a series of all possible and relavent flashcard for the user.
    The flashcards should be concise and should cover all the important points.
    You should respond as key value pairs where the key is the question and the value is the answer.
    For example: Your response should look like a python dictionary "Question 1": "Answer to Question 1", "Question 2": "Answer to Question 2"
    YOU WILL NEVER USE QUESTION NUMBERING IN YOUR RESPONSE. You will only provide the questions and answers.
    everything should be part of a single dictionary, i.e all the questions and answers should be part of a single dictionary.
    You will generate as many flashcards as possible. You will act as an expert in predicting where tricky questions
    can be formed and you will generate flashcards accordingly. You will leave no stone unturned in making the flashcards.
    Here is the document: {document}
    '''

    complete_prompt = f"{template.format(document = document)}"
    response = model.generate_content(complete_prompt)

    res = response.text

    ## updating the history
    history += f"Response: {res}\n"

    reply = res
    #print(res)
    return res





    
    



