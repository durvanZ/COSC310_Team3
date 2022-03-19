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
Lakshay Karnwal - Worked on creating a graphical user interface for the user using python module tkinter - to enter the text in a chatbox and see the history of chat on the display screen. Also worked on creating the test.py module. The test.py module uses pytest framework to test important functions of the chatbot.

#### GUI Implementation
![GUI Screenshot](https://user-images.githubusercontent.com/60047109/botdemo.png)

The GUI was implemented using the Python tkinter module for graphical interfaces. Using this module I was able to easily create a text box where the user enters their query/text. The text entered in the text box is then displayed on the GUI screen along with the Chatbot's response. This helps the user see the chat just like on any traditional chatting application. This helps the app become intuitivey easy-to-use for the user.

#### Test cases implementation
![Unit Testing Screenshot](https://user-images.githubusercontent.com/60047109/159101549-550633ec-41f7-408e-8fa5-5a43b64d2d75.png)

The Automated Unit Testing Framework used for this was pytest due to its easy to use module functions. I created multiple test cases for all the important functions which checks if all the functions are working as desired. You can run the Unit testing file using the pytest command. After running the test file, pytest displays a summary of failed and passed functions. If the functions do not pass that means the chatbot will have errors, if all the functions pass that means the program is working as desired.

In the screenshot example above, one of the functions failed because the value of probability was not correct. This is a useful feature as it reduces effort to debug the code.
