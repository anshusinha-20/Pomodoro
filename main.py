"""imported every class from the tkinter module"""
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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
"""created the window object"""
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

"""created canvas widget"""
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImage)
canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.pack()



"""loop to keep the window running"""
window.mainloop()