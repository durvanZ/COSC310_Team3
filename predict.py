from tensorflow.keras.models import load_model
import pickle
from nltk.sentiment import SentimentIntensityAnalyzer as mood
from nltk.stem import WordNetLemmatizer
import random
import numpy as np
import json
import nltk
nltk.download('vader_lexicon')

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pk1', 'rb'))
classes = pickle.load(open('classes.pk1', 'rb'))
model = load_model('chatbot_model.h5')


responses_outside_topics = ["I will connect you with our customer support team for further details.", "Could you please repeat that?", "I did not get that.", "I am not sure we have what you are looking for.", "Our customer support team will get in touch with you soon."]

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):  # convert sentence into a bag of word
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)  # initial bag with just 0z
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_classes(sentence):
    bow = bag_of_words(sentence)  # create a bag of words
    # predicts classes based on the bag of words
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25  # certin threshold so not much uncertainty
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        # first one is the index next one is the result
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list  # return list full of intents and probabilities


def get_response(intents_list, intents_json):
    diagnostic = str(intents_list)
    tag= intents_list[0]['intent']
    list_of_intents= intents_json['intents']
    result = random.choice(responses_outside_topics) ##default output
    ##print(list_of_intents)
    ## print(tag)

    for i in list_of_intents:
        if i['topics'] == tag:
            # assigns output messages to be printed
            result = random.choice(i['outputs'])
            break

    return result


def get_mood(user_input):  # sentiment analysis to add empathy to responses
    empathizer = mood()
    return empathizer.polarity_scores(user_input)


print("Yeaaaaah! Let's go. The bot is running babyyyy!")
empathy_response = ""
cat_vids = "https://www.youtube.com/results?search_query=cat+videos"
dank_memes = "https://www.reddit.com/r/dankmemes/"
res = ""
while True:
    message = input("")
    ints = predict_classes(message)
    usermood = get_mood(message)
    negative_vibes = usermood.get('neg')
    positive_vibes = usermood.get('pos')
    if (negative_vibes >= 0.6):
        empathy_response = random.choice(["I am really sorry to hear that", "We're sorry about that...",
                                         ":(( That's so unfortunate", "I understand your sentiment. Please allow me to help you, what do you need to know?"])
        res = empathy_response
        if (negative_vibes >= 0.7):
            res += random.choice(
                [f"Here are some cat videos: {cat_vids}", f"Here are some dank memes: {dank_memes}"])
    elif (positive_vibes >= 0.7):
        empathy_response = random.choice([":)", "Happy spring!!!", "I'm glad you're satistifed with my service",
                                         "Fantastic!!!", "Awesome", "I love to hear that", "You fill my heart with joy :))"])+"\n"
        res = empathy_response + get_response(ints, intents)
    print(res)
