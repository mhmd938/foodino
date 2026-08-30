import tkinter as tk
from tkinter import ttk
from food import Food, Meal, FoodApp

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("main_page")
        self.root.geometry("400x400")
        self.label = ttk.Label(self.root, text="hello")
        self.label.pack(pady=20)
        self.button = ttk.Button(self.root, text="click", command=self.on_click)
        self.button.pack(pady=10)
    
    def on_click(self):
        self.label.config(text="clicked")
    
    def run(self):
        self.root.mainloop()

def main():
    main_window = Window()
    main_window.run()

if __name__ == "__main__":
    main()