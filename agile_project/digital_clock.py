from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("400x150")

def update_time():
    current_time = strftime("%H:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, update_time)

label = Label(
    root,
    font=("Arial", 40, "bold"),
    bg="black",
    fg="lime"
)

label.pack(fill="both", expand=True)

update_time()

root.mainloop()