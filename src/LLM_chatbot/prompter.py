import openai
import json
from openai import OpenAI


def main():

    context_history = None

    #infinte loop for user asking questions to bot
    while(True):
        # 1. User asks a question
        user_input = input("Ask a question: ")

        # 2. Chatbot processes question with the JSON file of the stock the user is asking about
        user_reccomendation_prompt = make_reccomendation_prompt(user_input, context_history)
        chatbot_response = callGPT(user_reccomendation_prompt)

        # 3. Chatbot updates context history
        context_history =  "Q:" + user_input + "\nA:" + chatbot_response

        # Display to user
        print(chatbot_response)

    return 0


def make_reccomendation_prompt(user_input, previous_prompt):

    answer = ""

    #If the user has asked a question, take that into context
    if(previous_prompt == None):
        answer = previous_prompt

    ## Get the stock JSON file
    stock_json = open("data/stock_json/AAPL.json", "r")

    ## TODO: Treat JSON data as a string and append it to the prompt
    answer = answer + treat_json_as_string(stock_json)

    answer = answer + "Q: " + user_input
    return answer

def callGPT(prompt):
    ##GPT 4 calling
    client = OpenAI(api_key="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")
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {
                "role": "user",
                "content": [{"type": "text", "text": "Given the following context of conversation, of the form Q:{{question}} A:{{answer}} give an answer to the prompt of the user. If there is no context history and just a question, answer it to the best of your abilities. Remember to be precise in your answers, use detail to help the user to get as much useful information as he can obtain without overwhelming him with info. Here is the context history and the question, the question starts at Q:" + prompt}],
            }
        ],
        max_tokens = 300,
        )
    processed_response = response.choices[0].message.content
    return processed_response

def treat_json_as_string(json_file):
    json_string = json.dumps(json_file)
    return json_string