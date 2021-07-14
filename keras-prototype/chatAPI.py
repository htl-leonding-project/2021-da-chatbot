import flask
from flask import request
import json
from flask_cors import CORS

import numpy as np
import spacy
from tensorflow import keras


import pickle
import json

with open("intents.json") as file:
    data = json.load(file)
nlp = spacy.load("de_core_news_sm")

api = flask.Flask(__name__)
CORS(api)
api.config["DEBUG"] = True


@api.route('/api/ChatBot', methods=['GET'])
def home():
    inp = request.args.get('question', default='', type=str)
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
    return json.dumps({
        "message": response
    })


api.run(port=5000)
