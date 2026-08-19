import re
import tkinter as tk
from tkinter import ttk


class Food:
    def __init__(self, name, prefere_count):
        self.name = name
        self.prefered_count = prefere_count
        self.week_cook = 0
        self.month_cook = 0

class Meal:
    def __init__(self, food, date):
        self.food = food
        self.date = date

    def __str__(self):
        return f"Meal({self.food},{self.date})"
    
    @classmethod
    def str_to_meal(string):
        food_att = (re.findall(r"(\w*),", string))[0]
        date_att = (re.findall(r",(\d*-\d*-\d*)", string))[0]
        return Meal(food_att, date_att)

class FoodApp:
    def __init__(self):
        pass
# authnitcation section :
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
