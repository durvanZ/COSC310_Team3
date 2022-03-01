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
def bag_of_words(sentence): #convert sentence into a bag of word
    sentence_words= clean_up_sentence(sentence)
    bag= [0]* len(words) #initial bag with just 0z
    for w in sentence_words:
        for i, word in enumerate(words):
            if word== w:
                bag[i]= 1
    return np.array(bag)
def predict_classes(sentence):
    bow= bag_of_words(sentence) #create a bag of words
    res= model.predict(np.array([bow]))[0] #predicts classes based on the bag of words
    ERROR_THRESHOLD= 0.25 #certin threshold so not much uncertainty
    results= [[i,r] for i, r in enumerate(res) if r> ERROR_THRESHOLD]
    results.sort(key= lambda x: x[1], reverse= True)
    return_list= []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])}) #first one is the index next one is the result
    return return_list #return list full of intents and probabilities
def get_response(intents_list, intents_json):
    diagnostic = str(intents_list)
    tag= intents_list[0]['intent']
    list_of_intents= intents_json['intents']
    result = "Sorry, I can't understand what you mean, but here's my guess \n {0}".format(diagnostic) ##default output
    ##print(list_of_intents)
    ## print(tag)
    for i in list_of_intents:
        if i['inputs']== tag:
            result= random.choice(i['outputs']) #assigns output messages to be printed
            break
    return result

print("Yeaaaaah! Let's go. The bot is running babyyyy!")

while True:
    message= input("")
    ints= predict_classes(message)
    res= get_response(ints, intents)
    print(res)