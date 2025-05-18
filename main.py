from tkinter import *
from gtts import gTTS

import os

window = Tk()
window.title("Text-to-Speech Converter")
window.geometry("650x550")


frame1 = Frame(window,bg="Lime",height="150")
frame1.pack(fill=X)

frame2 = Frame(window, bg="Blue", height="400")
frame2.pack(fill=X)

title_label = Label(frame1, text="Text to Speech", font="Bold, 40",bg="Lime")
title_label.place(x="150",y="75")

entry = Entry(frame2, border=5, width=35, font=20)
entry.place(x="165",y="50")

def play():
    #Language in which you want to convert
    language = "en"

    # Passing the text  and language,
    # here we have slow=False. Which tells
    # the module that the converted audio should
    # have a high speed

    myobj = gTTS(text=entry.get(), lang=language, slow=False)

    # give the name as you want to
    # save the audio

    myobj.save("convert.wav")
    #play the audio using any software available in the system
    os.system("convert.wav")

button = Button(frame2, text="Submit",bg="Orange",pady=10,width=25,font="Bold, 15", command=play)
button.place(x="190",y="125")

window.mainloop()