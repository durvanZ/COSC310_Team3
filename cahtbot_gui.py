from predict import *
from tkinter import *

root = Tk()

message, ints, res, intents

def send():
    send = "You: " + e.get()
    txt.insert(END, "\n" + send)
    txt.insert(END, "\n" + res)
    e.delete(0, END)


txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=50) #
send = Button(root, text="Send", command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title("Customer Service Chatbot")
root.mainloop()

while True:
    message= e.get()
    ints= predict_classes(message)
    res= get_response(ints, intents)
    #print(res)
