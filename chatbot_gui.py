from predict import *
from tkinter import *

root = Tk()


def send():

    message = e.get()
    gui_output = "You: {0}".format(
        "*makes eye contact" if not message else message)
    txt.insert(END, "\n" + gui_output)
    ints = predict_classes(message)
    response_bot = "Bot: {0}".format(get_response(ints, intents))
    txt.insert(END, "\n" + response_bot)
    e.delete(0, END)


txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=50)
send = Button(root, text="Speak", command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title("Customer Service Chatbot")
txt.insert(END, "Click 'Speak' to interact with the customer service bot")

root.mainloop()
