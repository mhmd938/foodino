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
        # self.root = root
        # self.root.title("Food Management")
        # self.root.geometry("900x700")
        # self.root.configure(bg="#982525")
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
            week_cook INTEGER NOT NULL,
            month_cook INTEGER NOT NULL       
        )
        """)
        self.connection.commit()

    def add_food(self, food_name, prefere_count = 0):
        self.cursor.execute(
            "INSERT INTO foods (name, prefere_count, week_cook, month_cook) VALUES (?, ?, ?, ?)",
            (food_name, prefere_count, 0, 0)
        )
        self.connection.commit()

    def fetch_food(self):
        self.cursor.execute("SELECT * FROM foods")
        rows = self.cursor.fetchall()
        food_objects = []
        for row in rows:
            food_objects.append(Food(*row))
        return food_objects
    
    def add_meal(self, meal:str):
        self.cursor.execute(
            "INSERT INTO meals (meal) VALUES (?)",
            (meal,)
        )
        self.connection.commit()

    def fetch_meal(self) -> Meal:
        """Get data from database and retrun a list of Meal objects"""
        self.cursor.execute("SELECT * FROM meals")
        rows = self.cursor.fetchall()
        string_meals = [row[1] for row in rows]
        meals = list(map(Meal.str_to_meal, string_meals))
        return meals
    
    def collect_food_name(self):
        foods = FoodApp.fetch_food(self)
        foods_name = list(map(lambda food: food.name, foods))
        return foods_name
    
    def search_similar_foods(self, searched_food):
        foods_name = FoodApp.collect_food_name(self)
        similar = []
        for food in foods_name:
            if food == searched_food:
                similar.append(food)
        if similar:
            return similar
        
        for food in foods_name:
            if food[:3] == searched_food[:3] and len(searched_food) - 2 <= len(food) <= len(searched_food) + 2:
                if not food in similar:
                    similar.append(food)
            if len(set(food).intersection(set(searched_food))) >= 4 and len(searched_food) - 2 <= len(food) <= len(searched_food) + 2:
                if not food in similar:
                    similar.append(food)
        return similar

    def close_database(self):
        self.connection.close()