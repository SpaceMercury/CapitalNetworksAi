import openai
import json
from openai import OpenAI
import os
import pandas as pd

def make_reccomendation_prompt(stock, user_id, user_input, previous_prompt):

    answer = str("")

    #If the user has asked a question, take that into context
    if(previous_prompt == None):
        answer = previous_prompt

    ## Get the stock JSON file
    with open (f'data/{stock}.json') as f:
        ticker_json = json.load(f)

    ## Get the user JSON file
    with open (f'data/users/data_extracted_users/user{user_id}.json') as f:
        user_json = json.load(f)

    ##Treat JSON data as a string and append it to the prompt
    answer = f"{answer} Ticker Info:{ticker_json} User info:{user_json}"

    answer = answer + "Q: " + user_input
    return answer


def callGPT(prompt):
    ##GPT 4 calling
    key = os.environ["OPENAI_API_KEY"]
    client = OpenAI(api_key=key)
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {
                "role": "user",
                "content": [{"type": "text", "text": " Your name is shin, start every conversation with Shin: Given the following context of conversation, of the form Q:{{question}} A:{{answer}} give an answer to the prompt of the user. Treat the user well, greet him if it's the first time he is interacting with you. If there is no context history (it is the first time the user is asking a question)and a question, answer it to the best of your abilities. NEVER INCITE A USER TO BUY A STOCK, ONLY RELAY INFORMATION SO THE USER CAN MAKE AN INFORMED DECISION. Remember to be precise in your answers, use details from the context history about the company to help the user to get as much useful information as he can obtain without overwhelming him with info. To maybe better understand the user, think of other publicly traded companies that align with the interests of the user and use those to help yourself to give a more precise and adequate answer to the user, as well as using the data from the user given to you. Here is the context history and the question, the question starts at Q:" + prompt}],
            }
        ],
        max_tokens = 300,
        )
    processed_response = response.choices[0].message.content
    return processed_response
    
def produce_user_info(user_id):
    user_json = {}
    df = pd.read_csv(f'data/users/user{user_id}.csv')

    #add name of user in json
    user_json.update({"name": "Joseph"})

    investing = get_percentage_of_use(user_id, 'StockFeature_underlyingSymbol',"investing_percentages")
    user_json.update(investing)
    currency = get_percentage_of_use(user_id, 'CURRENCY', "currency_percentages")
    user_json.update(currency)

    with open(f'data/users/data_extracted_users/user{user_id}.json', 'w') as outfile:
        json.dump(user_json, outfile)



def get_percentage_of_use(user_id, feature, description):
    #get user info from csv
    df = pd.read_csv(f'data/users/user{user_id}.csv')
 
    #Group by stock ticker and count the number of times purchased
    df = df.groupby([feature]).size().reset_index(name='counts')

    total_stocks = df['counts'].sum()
    #Turn the count column into a percentage
    df['counts'] = df['counts']/total_stocks
    #Grab the pairs of percentages and stock tickers
    # and put them in a JSON to feed to LLM

    user_json = { description: []}
    for index, row in df.iterrows():
       user_json[description].append({row[feature]: row['counts']})
    
    return user_json

def chatrequest(stock, user_input):
    produce_user_info("3")
    context_history = None

    # 2. Chatbot processes question with the JSON file of the stock the user is asking about
    user_reccomendation_prompt = make_reccomendation_prompt(str(stock), "3", user_input,context_history)
    chatbot_response = callGPT(user_reccomendation_prompt)

    # 3. Chatbot updates context history
    context_history =  "Q:" + user_input + "\nA:" + chatbot_response

    # Display to user)

    return chatbot_response

def clickrequest(stock):
    # 1. Chatbot processes question with the JSON file of the stock the user is asking about
    user_reccomendation_prompt = make_reccomendation_prompt(str(stock), "3", "Give me some information about this stock in general, related to me and to the current circumstances", None)
    chatbot_response = callGPT(user_reccomendation_prompt)

    # Display to user)
    return chatbot_response


