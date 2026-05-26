from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    header.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

    checkmarks_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    checkmarks_label.config(text="✔"*(reps//2))
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        header.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
        reps=0

    elif reps % 2 == 0:
        header.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)

    else:
        header.config(text="WORK", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # print(count)
    count_min = count // 60
    count_sec = count % 60

    # if count_sec < 10:
    #     count_sec = f"0{count_sec}"
    # canvas.itemconfig(timer_text, text=f"{str(count_min).zfill(2)}:{str(count_sec).zfill(2)}")
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# window = Tk()
# window.title("Pomodoro")
# window.config(padx=100, pady=50, bg=YELLOW)
# def say_something(a, b, c, d):
#     print(a, b, c, d)

# window.after(1000, say_something, "I", "Am", "The", "Thing")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

header = Label(text="Timer", font=(FONT_NAME, 60, "bold"), fg=GREEN, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="Start", font=(FONT_NAME, 25, "bold"), highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", font=(FONT_NAME, 25, "bold"), highlightthickness=0, command=reset_timer)

checkmarks_label = Label(text="", font=(FONT_NAME, 10, "normal"), fg=GREEN, bg=YELLOW)

header.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
checkmarks_label.grid(column=1, row=3)

window.mainloop()