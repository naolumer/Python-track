from tkinter import *
BACKGROUND_COLOR= "#B1DDC6"
import pandas
import random
current_card={}
to_learn={}

try:
    data= pandas.read_csv("./DAY-31/data/words_to_learn.csv")

except FileNotFoundError:
    original_data= pandas.read_csv("./DAY-31/data/french_words.csv")
    to_learn= original_data.to_dict(orient="records")
else:
    to_learn= data.to_dict(orient= "records")

    

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text= current_card["French"], fill= "black")
    canvas.itemconfig(card_background, image= card_front_img)
    flip_timer= window.after(3000, func= flip_card)

def flip_card():
    canvas.itemconfig(title_text,text= "English", fill= "white")
    canvas.itemconfig(word_text, text= current_card["English"], fill= "white")
    canvas.itemconfig( card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("./DAY-31/data/words_to_learn.csv", index= False)
    
    next_card()
    
    

window= Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

flip_timer= window.after(3000, func= flip_card)


canvas= Canvas(width=800, height= 526)
card_front_img= PhotoImage(file= "./DAY-31/images/card_front.png")
card_back_img = PhotoImage(file="./DAY-31/images/card_back.png")
card_background=canvas.create_image(400, 263, image= card_front_img)
canvas.grid(column=0,row=0, columnspan=2)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)

word_text=canvas.create_text(400, 263, text="word", font=("Ariel", 40, "italic"))
title_text=canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "bold"))

check_image= PhotoImage("./DAY-31/images/right.png")
known_button= Button(image= check_image, highlightthickness=0, command= is_known)
known_button.grid(row=1, column=1)

cross_image= PhotoImage(file="./DAY-31/images/wrong.png")
unknown_button= Button(image= cross_image, highlightthickness=0, command=next_card )
unknown_button.grid(row=1, column=0)

next_card()





window.mainloop()