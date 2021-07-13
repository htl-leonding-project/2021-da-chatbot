import json

import colorama
import numpy as np
import spacy
from spacy import displacy
from tensorflow import keras

colorama.init()
from colorama import Fore, Style

import pickle

with open("intents.json") as file:
    data = json.load(file)
nlp = spacy.load("de_core_news_sm")


def chat():
    name = ''
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20

    print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
    while True:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        inp = input()
        if inp.lower() == "quit":
            f = open("log.txt", "a")
            f.write("QUITED CHATBOT\n")
            f.close()
            break

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                                                          truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                if tag == "name":
                    doc = nlp(inp)
                    for ent in doc.ents:
                        if ent.label_ == "PER":
                            name = ent.text.title()
                response = np.random.choice(i['responses'])
                response = response.replace("{name}", name)
                print(Fore.LIGHTRED_EX + "ChatBot:" + Style.RESET_ALL, response)
                f = open("log.txt", "a")
                f.write("User:" + inp + "\nBot:" + response + "\n")
                f.close()


chat()
