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

"""created the canvas widget"""
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImage)
canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

"""created the labelTimer object"""
labelTimer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
labelTimer.grid(row=1, column=2)
labelTimer.config(padx=20, pady=20)

"""created the labelCheck object"""
labelCheck = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
labelCheck.grid(row=4, column=2)
labelCheck.config(padx=20, pady=20)

"""created the buttonStart object"""
buttonStart = Button(text="Start")
buttonStart.grid(row=3, column=1)
buttonStart.config(padx=20, pady=20)

"""created the buttonReset object"""
buttonReset = Button(text="Reset")
buttonReset.grid(row=3, column=3)
buttonReset.config(padx=20, pady=20)


"""loop to keep the window running"""
window.mainloop()