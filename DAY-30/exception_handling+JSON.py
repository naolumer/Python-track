from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
window= Tk()
window.title("Password Manager")
window.config(padx=60,pady=60)

canvas= Canvas(width=200, height=200)
img_logo= PhotoImage(file="./DAY-30/logo.png")
canvas.create_image(100,100, image=img_logo)
canvas.grid(column=1,row=0)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '+', '&', '*', '(', ')']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def get_password():
    website=web_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email= data[website]["Email"]
            password= data[website]["Password"]
            messagebox.showinfo(title= website, message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
    
    
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
    new_data= {web: {"Email":ema,
                    "Password": passs}}

    if len(web)==0 or len(passs)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data= json.load(data_file)
        
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        
        else: 
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        
        finally:
            web_entry.delete(0,END)
            pass_entry.delete(0,END)


website=Label(text="Website:")
website.grid(row=1,column=0)

email= Label(text="Email/Username:")
email.grid(column=0, row=2)

password= Label(text="Password:")
password.grid(column=0, row=3)

web_entry= Entry(width=34)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_entry= Entry(width=44)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "naolumer3@gmail.com")

pass_entry= Entry(width=34)
pass_entry.grid(column=1, row=3)

generate_password= Button(text="Generate", command= pass_generator)
generate_password.grid(row=3,column=2)

search_button= Button(text="Search", command= get_password)
search_button.grid(row=1, column=2)

addd= Button(text="Add", width=37,command=save)
addd.grid(column=1,columnspan=2, row=4)


window.mainloop()