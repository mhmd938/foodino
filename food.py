import re
import sqlite3
from datetime import datetime
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
    def str_to_meal(cls, string):
        food_att = (re.findall(r"(\w*),", string))[0]
        date_att = (re.findall(r",(\d*-\d*-\d*)", string))[0]
        return cls(food_att, date_att)


class FoodApp:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY,
            meal TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def save_meal(self, meal:str):
        self.cursor.execute(
            "INSERT INTO meals (meal) VALUES (?)",
            (meal,)
        )
        self.connection.commit()

    def fetch_meal(self):
        self.cursor.execute("SELECT * FROM meals")
        meals = self.cursor.fetchall()
        for meal in meals:
            print(meal)
    def close_database(self):
        self.connection.close()