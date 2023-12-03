# CapitalNetworksAi

## LauzHack 2023 - CapitalNetworksAI

## Overview

Personalized stock reccomendation system based on user's risk profile, preferences, and previous investments. After generating reccomendations for the user, the user can interact with a chatbot to learn more about the stocks and make a decision. The LLM chatbot has a context of the user's previous interactions and can provide more personalized information.

## Team Members

- Amit
- Eduardo
- Pol

## Features

- Data creation and cleaning
- Personalized reccomendation system
- AI chatbot

### LLM Chatbot

The LLM chatbot uses the GPT-4-turbo model to generate responses. The LLM model is a language model that uses a prompt to generate a response. The prompt is a concatenation of the user's previous messages and the chatbot's previous responses. The LLM model is trained on the Reddit dataset. The LLM model is prompted with the user's previous messages and the chatbot's previous responses. The model is then used to generate a response to the user's message. We used a number of techniques from different sources to improve the performance of the LLM model through prompt engineering.

### Installation and execution

Start by cloning the repo locally, then you will need to associate an API key to the project from OpenAI as we are using GPT-4-turbo. Once you have that set up, there is a demo.py file that you need to run, which consists of the graphical interface to be able to use our chatbot and implementation algorithm. Make sure you have all the dependencies installed, there is a requirements.txt, and after that you are good to go!

---
