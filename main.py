# import tkinter module
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    tk_window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text = "TIMER" ,fg=GREEN)
    mark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    if(reps >= 8):
        count_down(LONG_BREAK_MIN, 0)
        timer_label.config(text = "BREAK" ,fg=RED)
    elif reps % 2 == 0:
        count_down(WORK_MIN, 0)
        timer_label.config(text = "WORK", fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN, 0)
        timer_label.config(text = "BREAK" , fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# in order to use a counter we used recursion to call the method every second
def count_down(minutes, seconds):
    if minutes < 10:
        text_1 = "0"
    else:
        text_1 = ""
    if (seconds < 10):
        text_2 = "0"
    else:
        text_2 = ""
    global timer
    canvas.itemconfig(timer_text, text=f"{text_1}{minutes}:{text_2}{seconds}")
    if (seconds > 0 and minutes > 0):
        timer = tk_window.after(1000, count_down, minutes, seconds - 1)
    elif (seconds <= 0 and minutes > 0):
        timer = tk_window.after(1000, count_down, minutes - 1, 59)
    elif(seconds > 0 and minutes == 0):
        timer = tk_window.after(1000, count_down, 0, seconds-1)
    else:
        global reps
        if reps % 2 == 0:
            mark_label.config(text=mark_label.cget("text") + "✔")
        reps+=1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

tk_window = Tk()
tk_window.title("Pomodoro")
tk_window.config(padx=100, pady=50)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.config(bg=YELLOW)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label()
timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 60, "bold"))
timer_label.grid(column=1, row=0)

mark_label = Label()
mark_label.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
mark_label.grid(column=1, row=3)


def action():
    pass


start_button = Button(text="Start", fg='black', bg=YELLOW, font=(("Times New Roman"), 15), highlightthickness=-1, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", fg='black',
                       bg=YELLOW, font=(("Times New Roman"), 15), highlightthickness=-1, command=reset_timer)
reset_button.grid(column=2, row=2)

tk_window.config(bg="#f7f5dd")
tk_window.mainloop()
