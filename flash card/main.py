from tkinter import * 
import pandas 
import random

BACKGROUND_COLOR = "#B1DDC6"

windows = Tk()
windows.title("Flash Card Game")
windows.config(padx=50 , pady= 50 , bg=BACKGROUND_COLOR )


#----- read csv  -------------------#
try :
    data_frame = pandas.read_csv("newcsv.csv")
except FileNotFoundError :
    data_frame = pandas.read_csv("french_words.csv")
finally:
    data = data_frame.to_dict("records")


#----- change word push button  -------------------#

def new_french_word():
    global timer ,choice_word
    windows.after_cancel(timer)
    choice_word = random.choice(data)
    word = choice_word["French"]
    canvas.itemconfig(canvas_image,image=front_photo)
    canvas.itemconfig(language_text,fill="black") 
    canvas.itemconfig(word_text,fill="black") 
    canvas.itemconfig(word_text, text=word)
    canvas.itemconfig(language_text, text="French")
   
    timer = windows.after(3000,new_english_word)

def new_english_word():
    global choice_word
    word = choice_word["English"]
    canvas.itemconfig(canvas_image,image=back_photo)
    canvas.itemconfig(language_text,fill="white") 
    canvas.itemconfig(word_text,fill="white") 
    canvas.itemconfig(word_text, text=word)
    canvas.itemconfig(language_text, text="English")


def remove_word ():
    data.remove(choice_word)
    new_word = pandas.DataFrame(data)
    new_word.to_csv("newcsv.csv", index=False)
    new_french_word()


#----- GUI -------------------#

#----- Button -----#
cancel_button_photo = PhotoImage(file="wrong.png")
cancel_button = Button(image=cancel_button_photo,command=new_french_word,highlightthickness=0)
cancel_button.grid(row=1, column=0)

accept_button_photo = PhotoImage(file="right.png")
accept_button = Button(image=accept_button_photo,command=remove_word,highlightthickness=0)
accept_button.grid(row=1, column=1)

#----- Canvas -----#
canvas = Canvas(width=800,height=526,highlightthickness=0, bg=BACKGROUND_COLOR)
front_photo = PhotoImage(file="card_front.png")
back_photo = PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(400,263,image=front_photo)
canvas.grid(row=0,column=0,columnspan=2)

#----- Label -----#
language_text = canvas.create_text(400, 150, text="", fill="black", font=('arial 40 italic'))
word_text = canvas.create_text(400, 263, text="", fill="black", font=('arial 60 bold'))

timer = windows.after(3000,new_english_word)

new_french_word()


windows.mainloop()