# Hudson's Drip™ customer service AI Chatbot

  We created a chatbot to serve the customers of an online clothing store. We used artificial intelligence and machine learning and followed agile SDLC methodologies. Hence, our development cycle consisted of a scrum in which basic functionality was the goal for this first iteration.
  
  Our software consists of two input JSON files used to train the neural network and make personalized answers based on customer information. The training.py imports data from intents.py and trains the neural network. training.py outputs words and classes pk1 files, which are used by the predict.py module to estimate the probability that a user input addresses a particular topic in the intents.JSON. A random response from the most likely topic is outputted by the chatbot. At the current stage, the chatbot is able to estimate the topic, and fully conversational functionality is still under development.

Several libraries were used: random, json, pickle, numpy, nltk, and tensorflow.

[JIRA Roadmap](https://durvan.atlassian.net/jira/software/projects/CT3/boards/).  
[Reference material](https://www.youtube.com/watch?v=1lwddP0KUEg).  
  
## COSC 310 Group members:
- Guiherme Durvan Zandamela
- Lakshay Karnwal (37530722)
- Abdulaziz Almutlaq
- Ravil Bigvava
- Jordan onwuvuche

### Assignment 2 tasks:
Lakshay Karnwal - Worked on creating a graphical user interface for the user to enter the text in a chatbox and see the history of chat on the display screen. Also worked on creating the test.py module. The test.py module uses pytest framework to test important functions of the chatbot.

![GUI Screenshot]("https://user-images.githubusercontent.com/60047109/159101357-051933d3-6567-40e7-bb1d-87293c75a9fe.png")
