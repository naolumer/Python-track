from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

window= Tk()
window.title("Password Manager")
window.config(padx=60,pady=60)

canvas= Canvas(width=200, height=200)
img_logo= PhotoImage(file="./DAY-29/logo.png")
canvas.create_image(100,100, image=img_logo)
canvas.grid(column=1,row=0)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '+', '&', '*', '(', ')']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def pass_generator():
    
    password_letters=[choice(letters) for i in range(randint(8,10))]
    password_symbols=[choice(symbols) for i in range(randint(2,4))]
    password_numbers=[choice(numbers) for i in range(randint(2,4))]

    password_list= password_letters+password_symbols+password_numbers
    shuffle(password_list)
    generated_password= "".join(password_list)
    pass_entry.insert(0, generated_password)

    pyperclip.copy(generated_password)

def save():
    web=web_entry.get()
    ema=email_entry.get()
    passs=pass_entry.get()

    if len(web)==0 or len(passs)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=web, message= f"These are the details you entered: \nEmail:{ema}\nPassword:{passs}\n Is it ok to save")
        if is_ok:
            with open("./DAY-29/data.txt", "a") as data_file:
                data_file.write(f"{web} | {ema} | {passs}\n")
                web_entry.delete(0,END)
                pass_entry.delete(0,END)


website=Label(text="Website:")
website.grid(row=1,column=0)

email= Label(text="Email/Username:")
email.grid(column=0, row=2)

password= Label(text="Password:")
password.grid(column=0, row=3)

web_entry= Entry(width=44)
web_entry.grid(column=1, columnspan=2, row=1)
web_entry.focus()

email_entry= Entry(width=44)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "naolumer3@gmail.com")

pass_entry= Entry(width=34)
pass_entry.grid(column=1, row=3)

generate_password= Button(text="Generate", command= pass_generator)
generate_password.grid(row=3,column=2)

addd= Button(text="Add", width=37,command=save)
addd.grid(column=1,columnspan=2, row=4)


window.mainloop()