import re
import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import ttk


class Food:
    def __init__(self, name, prefere_count, week_cook, month_cook):
        self.name = name
        self.prefered_count = int(prefere_count)
        self.week_cook = int(week_cook)
        self.month_cook = int(month_cook)

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
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS foods (
            name TEXT NOT NULL,
            prefere_count INTEGER NOT NULL,
            week_count INTEGER NOT NULL,
            month_count INTEGER NOT NULL        
        )
        """)
        self.connection.commit()

    def fetch_food(self):
        self.cursor.execute("SELECT * FROM foods")
        rows = self.cursor.fetchall()
        food_objects = []
        for row in rows:
            food_objects.append(Food(*row))
        return food_objects

    def save_meal(self, meal:str):
        self.cursor.execute(
            "INSERT INTO meals (meal) VALUES (?)",
            (meal,)
        )
        self.connection.commit()

    def fetch_meal(self):
        """Get data from database and retrun a list of Meal objects"""
        self.cursor.execute("SELECT * FROM meals")
        rows = self.cursor.fetchall()
        string_meals = [row[1] for row in rows]
        meals = list(map(Meal.str_to_meal, string_meals))
        return meals
    
    def close_database(self):
        self.connection.close()
app = FoodApp()