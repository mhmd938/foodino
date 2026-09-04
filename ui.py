import tkinter as tk
from tkinter import ttk
from food import Food, Meal, FoodApp

class FoodTemplate(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)
        tk.Label(self, text="food name").pack()


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("main_page")
        self.geometry("400x400")
        self.label = ttk.Label(self, text="hello")
        self.label.pack(pady=20)
        self.button = ttk.Button(self, text="click", command=self.on_click)
        self.button.pack(pady=10)
        self.food_frame = FoodTemplate(self)
        self.food_frame.pack()
    
    def on_click(self):
        self.label.config(text="clicked")
    
    def run(self):
        self.mainloop()

def main():
    main_window = Window()
    main_window.run()

if __name__ == "__main__":
    main()