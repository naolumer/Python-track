
import tkinter

def button_clicked():
    print("button got clicked")
    new_text= input.get()
    my_label.config(text= new_text)

window= tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500,height= 300)

my_label= tkinter.Label(text="My label", font=("Arial", 24,"bold"))
my_label.config(text= "New text")
my_label.pack(side="left")

button= tkinter.Button(text= "click me", command= button_clicked)
button.pack(side="left")

def add(*args):
    return sum(args)
summ= add(2,3,4,5,6)
print(summ)

# Entry
input= tkinter.Entry(width=10)
input.pack(side="left")
print(input.get())




    







window.mainloop()