# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
import numpy as np
import json
import nltk
from nltk.stem import WordNetLemmatizer
import pickle

from tensorflow.keras.models import load_model
lemmatizer= WordNetLemmatizer()
intents= json.loads(open('intents.json').read())
words= pickle.load(open('words.pk1', 'rb'))
classes= pickle.load(open('classes.pk1', 'rb'))
model= load_model('chatbot_model.model')

def clean_up_sentence(sentence):
    sentence_words= nltk.word_tokenize(sentence)
    sentence_words= [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words
def bag_of_words(sentence):
    sentence_words= clean_up_sentence(sentence)
    bag= [0]* len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word== w:
                bag[i]= 1
    return np.array(bag)
def predict_classes(sentence):
    bow= bag_of_words(sentence)
    res= model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD= 0.25
    results= [[i,r] for i, r in enumerate(res) if r> ERROR_THRESHOLD]
    results.sort(key= lambda x: x[1], reverse= True)
    return_list= []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list
def get_response(intents_list, intents_json):
    tag= intents_list[0]['intent']
    list_of_intents= intents_json['intents']
    result = "Sorry, I can't understand what you mean" ##default output
    for i in list_of_intents:
        if i['inputs']== tag:
            result= random.choice(i['outputs'])
            break
    return result

print("Yeaaaaah! Let's go. The bot is running babyyyy!")

while True:
    message= input("")
    ints= predict_classes(message)
    res= get_response(ints, intents)
    print(res)