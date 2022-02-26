import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for input in intent['inputs']:
        word_list = nltk.word_tokenize(input)
        words.extend(word_list)
        documents.append(word_list, intent['tag'])
        if intent['tag'] not in classes:
            classes.append(intent['topics'])

words = [lemmatizer.lemmatize(word)
         for word in words if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words, open('words.pk1', 'wb'))
pickle.dump(words, open('classes.pk1', 'wb'))

training = []
putput_empty = [0] + len(classes)

for document in documents:
    bag = []
    word_inputs = document[0]
    word_inputs = [lemmatizer.lammetize(word.lower()) for word in word_inputs]
    for word in words:
        bag.append(1) if word in word_inputs else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd, metrics=['accuracy'])

model.fit(np.array(train_x), np.array(train_y),
          epochs=200, batch_size=5, verbose=1)
model.save('cahtbot_model.model')
print("Done")
