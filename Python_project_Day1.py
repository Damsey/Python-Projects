import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%Y, %m, %d; %H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, update_clock)

app = tk.Tk()
app.title("Python clock")

clock = tk.Label(app, text = "", font=("Helvetica", 48))
clock.pack()

update_clock()
app.mainloop()
