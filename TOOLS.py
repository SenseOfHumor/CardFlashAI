import json

## function to get the dictionary from the response
questions = []
answers = []

def get_dict(reply):
    dict_from_reply = json.loads(reply)
    for key, value in dict_from_reply.items():
        questions.append(key)
        answers.append(value)

        #print(f"Question: {key}, Answer: {value}")

    return dict_from_reply