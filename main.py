from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFA27F"
RED = "#e7305b"
GREEN = "#97BE5A"
YELLOW = "#FFE8C5"
FONT_NAME = "Courier"
WORK_MIN = 1500
SHORT_BREAK_MIN = 300   
LONG_BREAK_MIN = 1200
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global check
    global reps
    global timer

    window.after_cancel(timer)

    reps = 0
    canvas.itemconfig(count_text, text='00:00')

    lbl.config(text='GOJE!',fg=RED)

    check =''
    check_lbl.config(text=check)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps

    reps += 1
    if reps > 8:
        reps = 1

    if reps % 8 == 0:
        lbl.config(text='BREAK', fg=RED)
        countdown(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        lbl.config(text='BREAK', fg=RED)
        countdown(SHORT_BREAK_MIN)
    else:    
        lbl.config(text='WORK', fg=GREEN)
        countdown(WORK_MIN)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global check
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(count_text, text=f'{count_min:02d}:{count_sec:02d}')
    

    if count > 0:
        timer = window.after(1000,countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check += '✔'
            check_lbl.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("GOJE!")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=214, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato2.png')
canvas.create_image(107,112,image=tomato_img)
count_text = canvas.create_text(103,121,text='00:00',fill='white',font=(FONT_NAME,27,'bold'))
canvas.grid(column=1,row=1,pady=20)

lbl = Label(text='GOJE!',bg=YELLOW,fg=RED,font=(FONT_NAME,30,'bold'))
lbl.grid(column=1,row=0)

btn = Button(text='START',command=start_timer)
btn.grid(column=0,row=2)

btn = Button(text='RESET',command=reset)
btn.grid(column=2,row=2)

check = ''
check_lbl = Label(text=check,bg=YELLOW,fg=GREEN,font=(FONT_NAME,15,'bold'))
check_lbl.grid(column=1,row=3)

window.mainloop()