# Pomodoro
from tkinter import *
import math

# number of work repetitions before a long break
WORK_MIN = 0.5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# colors for easier access
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reps=0
timmer= None

window= Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=GREEN)

def reset_timer():
    window.after_cancel(timmer)
    canvas.itemconfig(timer_text, text= "00:00")
    timer.config(text="Timer")
    checkmark.config(text="")

def start_timer():
    global reps
    reps+=1
    work_min= int(WORK_MIN*60)
    short_break= int(SHORT_BREAK_MIN*60)
    long_break= int(LONG_BREAK_MIN*60)
    
    if reps%8==0:
        count_down(long_break)
        timer.config(text="Break", fg=RED)
    elif reps%2==0:
        count_down(short_break)
        timer.config(text="Break", fg=RED)
    else:
        count_down(work_min)
        timer.config(text="Work", fg=PINK)
    
    

def count_down(count):
    count_min= math.floor(count/60)
    count_sec= count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count>0:
        global timmer
        timmer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=""
        work_sessions= math.floor(reps/2)
        for i in range(work_sessions):
            marks+="✓"
            checkmark.config(text=marks)

canvas=Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img=PhotoImage(file="./DAY-28/tomato.png")
canvas.create_image(100,112, image= tomato_img)

timer_text=canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(column=1,row=1)

start= Button(text="Start", highlightthickness=0,font=(FONT_NAME,20),command= start_timer)
start.grid(column=0,row=2)

reset=Button(text="Reset", highlightthickness=0, font=(FONT_NAME,20), command= reset_timer)
reset.grid(column=2,row=2)

timer= Label(text="Timer",fg=RED,bg=GREEN ,font=(FONT_NAME, 50))
timer.grid(column=1,row=0)

checkmark= Label(fg= RED,bg=GREEN,font=(FONT_NAME,20))
checkmark.grid(column=1,row=3)


window.mainloop()