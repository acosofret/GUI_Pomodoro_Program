from tkinter import *
import math
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
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text="00:00")
	title_label.config(text="Timer", fg=GREEN)
	progress_label.config(text="")
	global reps
	reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	global reps
	reps += 1
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60
	# If it's the 8th rep:
	if reps % 8 == 0:
		count_down(long_break_sec)
		title_label.config(text="BREAK", fg=RED)
	# If it's 2nd/4th/6th rep:
	elif reps % 2 == 0:
		count_down(short_break_sec)
		title_label.config(text="break", fg=PINK)
	# If it's the 1st/3rd/5th/7th rep:
	else:
		count_down(work_sec)
		title_label.config(text="WORK", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

	count_min = math.floor(count / 60)
	count_sec = count % 60
	if count_min < 10:
		count_min = f"0{count_min}"
	if count_sec < 10:
		count_sec = f"0{count_sec}"

	canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
	if count > 0:
		global timer
		timer = window.after(1000, count_down, count-1)
	else:
		start_timer()
		marks = ""
		work_sessions = math.floor(reps/2)
		for _ in range(work_sessions):
			marks += "✓"
		progress_label.config(text=marks)
		# my way of doing it below:
		# if reps % 2 == 0:
		# 	progress_label.config(text=f"{progress_label["text"]}\n✓")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)
# highlightthickness argument above is to hide the edges of the canvas that were still white (doesn't work on windows)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomate_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomate_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 32, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

progress_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
progress_label.grid(column=1, row=3)



window.mainloop()