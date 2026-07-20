import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_label,text="TIMER")
    canvas.itemconfig(timer_text,text="00:00")
    canvas.itemconfig(check_mark,text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global reps
    reps+=1
    Work_sec=WORK_MIN*60
    Short_break_sec=SHORT_BREAK_MIN*60
    Long_break_sec=LONG_BREAK_MIN*60
    
    if reps%8==0:
        count_down(Long_break_sec)
        canvas.itemconfig(timer_label,text="Break",fill=RED)
    if reps%2==0:
        count_down(Short_break_sec)
        canvas.itemconfig(timer_label,text="Break",fill=PINK)
    else:
        count_down(Work_sec)
        canvas.itemconfig(timer_label,text="WORK",fill=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        timer()
        marks=''
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            marks+="✔️"
            canvas.itemconfig(check_mark,text=marks)
        
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("POMODORO")
window.minsize(width=450,height=450)
canvas=Canvas(width=450,height=450,bg=YELLOW,highlightthickness=0 )
tamatar_png=PhotoImage(file="tomato.png")
canvas.create_image(225,225,image=tamatar_png)  
timer_text=canvas.create_text(225,245,text="00:00",fill="White",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=3)
timer_label=canvas.create_text(225,90,text="TIMER",fill="#9bdeac",font=(FONT_NAME,45,"bold"))

check_mark=canvas.create_text(250,370,text="",fill="#9bdeac",font=(FONT_NAME,10,"bold"))
Start=Button(text="Start",command=timer)
Reset=Button(text="Reset",command=reset_timer)


canvas.create_window(120,350,window=Start)
canvas.create_window(350,350,window=Reset)





window.mainloop()