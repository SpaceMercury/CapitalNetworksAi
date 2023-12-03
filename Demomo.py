import PySimpleGUI as sg
import random as rd
import src.LLM_chatbot.prompter as chatbot

# Define the advisor function
def advisor(stock, features):
    return f"Advice for {stock}: Based on the features {', '.join(features.keys())}, here's some advice..."

# Define the chatbot function
def Chat(txt):
    return chatbot.chatrequest(last_stock_clicked, txt)

# Define the function to get the best 5 stocks
def get_best_5_stocks():
    return chatbot.clickrequest

# Define the function to get the best stock features
def get_the_best_stock_features_that_user_likes():
    return ['Price', 'Volume', 'Market Cap', 'P/E Ratio', 'Dividend Yield']

# Function to initialize stock features with random values
def initialize_stock_features():
    return {stock: {feature: round(rd.uniform(100, 500), 2) for feature in get_the_best_stock_features_that_user_likes()} for stock in get_best_5_stocks()}

# Function to update each stock feature by a small step
def update_stock_features():
    for stock in stocks_features:
        for feature in stocks_features[stock]:
            stocks_features[stock][feature] *= round(rd.uniform(1.00, 1.01), 2)

# Function to create stock summary text
def create_stock_summary():
    summary_text = ""
    for stock, features in stocks_features.items():
        feature_summary = ", ".join([f"{k}: {v:.2f}" for k, v in features.items()])
        summary_text += f"{stock}: {feature_summary}\n\n"
    return summary_text

last_stock_clicked = AAPL
# Define colors and font styles
bg_color = '#f5f5f5'
text_color = '#333333'
button_color = ('white', '#ff8c00')  # Orange color for buttons
font_large = ("Arial", 22, 'bold')
font_medium = ("Arial", 18)
font_small = ("Arial", 14)

# Window size
window_width, window_height = 1524, 968

# Layout definition
layout = [
    [sg.Text("Stock Advisor", size=(int(window_width/12), 1), font=font_large, text_color=text_color)],
    [sg.HorizontalSeparator()],
    [sg.Button(stock, size=(15, 2), font=font_medium, button_color=button_color, border_width=2) for stock in get_best_5_stocks()],
    [sg.Text("Stock Information", font=font_medium)],
    [sg.Text("", font=font_medium, key='-FEATURES-', size=(200, 10))],
    [sg.Text("", key='-ADVISOR-', size=(200, 10), font=font_small)],
    [sg.HorizontalSeparator()],
    [sg.Text("Ask Shin", font=font_large)],
    [sg.InputText(key='-CHATINPUT-', size=(200, 10), font=font_small), sg.Button('Send', size=(10, 1), font=font_medium, button_color=button_color, border_width=2)],
    [sg.Text("", key='-CHATRESPONSE-', size=(200, 10), font=font_small)],
    [sg.Column([[]], expand_x=True), sg.Button('Exit', size=(10, 2), font=font_small, button_color=('#f0f0f0', '#d9534f'), border_width=2)]
]

# Create the window
window = sg.Window('AI Networks Group Stock Advisor', layout, size=(window_width, window_height), background_color=bg_color)

# Initial stock features
stocks_features = initialize_stock_features()
window['-FEATURES-'].update(create_stock_summary())

# Event Loop
while True:
    event, values = window.read(timeout=3000)  # Update every 3000 milliseconds (3 seconds)
    if event in (None, 'Exit'):
        break

    update_stock_features()
    window['-FEATURES-'].update(create_stock_summary())

    if event in get_best_5_stocks():
        last_stock_clicked = event
        stock_features = stocks_features[event]
        advice = advisor(event, stock_features)
        window['-ADVISOR-'].update(advice)

    if event == 'Send':
        chat_response = Chat(values['-CHATINPUT-'])
        window['-CHATRESPONSE-'].update(chat_response)

# Close the window
window.close()

