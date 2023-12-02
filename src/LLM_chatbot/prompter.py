import openai
import json
from openai import OpenAI





def main():

    # 1. User asks a question
    user_input = input("Ask a question: ")

    # 2. Chatbot processes question with the JSON file of the stock the user is asking about
    user_question_reccomendation_prompt = make_reccomendation_prompt(user_input);
    callGPT(user_question_reccomendation_prompt);


    return 0;


def make_reccomendation_prompt():

    ## Get the stock JSON file
    stock_json = open("data/stock_json/AAPL.json", "r")

    ## TODO: Treat JSON data as a string and append it to the prompt
    

    return "The stock we are interested has the following ticker: ‘AAPL’. We also have the stock vector"++"Consider the following user with this characteristic vector:"++". Would you recommend this stock to this specific user, and for what reasons list in order of importance."

def callGPT(prompt):
    ##GPT 4 calling
    client = OpenAI(api_key="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")
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
        max_tokens = 300,
        )
    processed_response = response.choices[0].message.content
    return processed_response


prompt = "The stock we are interested has the following ticker: ‘AAPL’. We also have the stock vector"++"Consider the following user with this characteristic vector:"++". Would you recommend this stock to this specific user, and for what reasons list in order of importance."

