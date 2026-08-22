import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("500x500")
label_1 = ttk.Label(window, text="enter your name")
label_1.pack(padx=5, pady=5)
entry = ttk.Entry(window, width=30)
entry.pack(padx=5)
hello_label = ttk.Label(window, text="")
hello_label.pack(pady=5)
def say_hello():
    name = entry.get()
    if name:
        hello_label.config(text=f"welcom to foodino {name}")
    else:
        hello_label.config(text=f"please enter your name")
button = ttk.Button(window, text="sign in", command=say_hello)
button.pack(pady=5)
window.mainloop()