# Hudson's Drip customer service AI Chatbot

  We created a chatbot to serve the customers of an online clothing store. We used artificial intelligence and machine learning and followed agile SDLC methodologies. Hence, our development cycle consisted of a scrum in which basic functionality was the goal for this first iteration.
  
  Our software consists of two input JSON files used to train the neural network and make personalized answers based on customer information. The training.py imports data from intents.py and trains the neural network. training.py outputs words and classes pk1 files, which are used by the predict.py module to estimate the probability that a user input addresses a particular topic in the intents.JSON. A random response from the most likely topic is outputted by the chatbot. At the current stage, the chatbot is able to estimate the topic, and fully conversational functionality is still under development.

Several libraries were used: random, json, pickle, numpy, nltk, and tensorflow.

[JIRA Roadmap](https://durvan.atlassian.net/jira/software/projects/CT3/boards/)
  
## COSC 310 Group members:
- Guiherme Durvan Zandamela
- Lakshay Karnwal
- Abdulaziz Almutlaq
- Ravil Bigvava
- Jordan onwuvuche


