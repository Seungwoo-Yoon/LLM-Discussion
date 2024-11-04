from openai import OpenAI
from prompt import *

def chatgpt(messages, api_key):
    while True:
        try:
            client = OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=1.0,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except:
            print('chat gpt error occured. redo.')

def prompt1(question):
    return user_prompt1.format(question)

def prompt2(round, opinions):
    opinions_except_me = ["" for i in range(len(opinions))]
    for i, opinion in enumerate(opinions):
        opinion_prompt = f"Participant {i}:\n{opinion}\n\n"
        for j in range(len(opinions_except_me)):
            if i != j:
                opinions_except_me[j] += opinion_prompt

    for i in range(len(opinions_except_me)):
        opinions_except_me[i] = user_prompt2.format(round, "initial" if round == 0 else "updated", opinions_except_me[i])
    
    return opinions_except_me

def extract_answer(question, response, api_key):
    prompt = answer_extract_prompt

    prompt += f"Question: \n{question} \n\n"

    prompt += f"Response: \n{response} \n\nExtraction: \n"

    messages = [
        {"role": "user", "content": prompt}
    ]
    
    return chatgpt(messages, api_key)

def score_answer(question, ground_truth, response, api_key):
    # prompt = scoring_prompt.format(question, ground_truth, response)

    # messages = [
    #     {"role": "user", "content": prompt}
    # ]
    
    # score = chatgpt(messages, api_key)

    # if "1" in score:
    #     return 1
    # else:
    #     return 0

    return ground_truth == response
