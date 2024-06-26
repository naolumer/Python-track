import tkinter

window= tkinter.Tk()
window.title("Miles to Km converter")
window.minsize(width=300, height=100)


my_label= tkinter.Label(text="Is equal to:", font=("Arial", 20, "normal"))
my_label.grid(column=1, row=2)

result_label= tkinter.Label(text=0, font=("Arial", 20, "normal"))
result_label.grid(column=2, row=2)

miles= tkinter.Label(text="miles", font= ("Arial", 20, "normal") )
miles.grid(column=3, row=1)

km= tkinter.Label(text="km", font= ("Arial", 20, "normal") )
km.grid(column=3, row=2)

def converter():
    mm=int(inputt.get())
    miles=mm*1.6
    r_miles= round(miles,2)
    result_label.config(text= r_miles)
    
calculate= tkinter.Button(text="Calculate", command= converter)
calculate.grid(column=2, row=3)

inputt= tkinter.Entry(width=8)
inputt.grid(column=2, row=1)


window.mainloop()