import tkinter as tk
from tkinter import ttk
from food import Food, Meal, FoodApp

class FoodTemplate(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, bg="yellow")
        self.food_label = tk.Label(self, text="food name")
        self.food_label.pack()
        self.food_entry = tk.Entry(self)
        self.food_add_button = tk.Button(self, text="add")
        self.food_entry.pack()
        self.food_add_button.pack()


class MealTemplate(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, bg="green")
        self.meal_label = tk.Label(self, text="meal name")
        self.meal_label.pack()


class ChartTemplate(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, bg="red")
        self.chart_label = tk.Label(self, text="chart name")
        self.chart_label.pack()


class SuggestionTemplate(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, bg="lightblue")
        self.suggestion_label = tk.Label(self, text="suggestion name")
        self.suggestion_label.pack()


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("main_page")
        self.geometry("1200x800")
        self.resizable(width=False, height=False)
        self.food_frame = FoodTemplate(self)
        self.food_frame.grid(row=1, column=0, sticky="nsew")
        self.meal_frame = MealTemplate(self)
        self.meal_frame.grid(row=1,column=1, sticky="nsew")
        self.chart_frame = ChartTemplate(self)
        self.chart_frame.grid(row=0, column=0, sticky="nsew", columnspan=3)
        self.suggestion_frame = SuggestionTemplate(self)
        self.suggestion_frame.grid(row=1, column=2, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=2)


    def on_click(self):
        self.label.config(text="clicked")
    
    def run(self):
        self.mainloop()

def main():
    main_window = Window()
    main_window.run()

if __name__ == "__main__":
    main()