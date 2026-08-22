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
