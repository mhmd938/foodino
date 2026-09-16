import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from food import Food, Meal, FoodApp

food_app = FoodApp()


class FoodAppButton(tk.Button):
    def __init__(self, master=None, text="", command=""):
        super().__init__(master, bg="white", width=9, height=1, text=text,
                         cursor="hand2", command=command, border=1,
                         relief="solid", fg="black")


class FoodTemplate(tk.Frame):
    def __init__(self, window, parent, foodapp=food_app):
        super().__init__(master=parent, bg="yellow")
        self.window = window
        self.foodapp = foodapp
        self.food_label = tk.Label(self, text="food name", bg="yellow")
        self.food_label.pack(pady=(10, 0))
        self.food_entry = tk.Entry(self)
        self.food_entry.pack()
        self.food_add_button = FoodAppButton(master=self, text="add",
                                             command=self.add_food_button)
        self.food_add_button.pack(pady=5)

        self.list_label = tk.Label(self, text="Food List", bg="yellow",
                                   font=("Arial", 10, "bold"))
        self.list_label.pack(pady=(15, 0))
        self.food_listbox = tk.Listbox(self, height=15, width=30)
        self.food_listbox.pack(pady=5, padx=10, fill="both", expand=True)

        self.refresh_food_list()

    def refresh_food_list(self):
        self.food_listbox.delete(0, tk.END)
        for food in self.foodapp.fetch_food():
            self.food_listbox.insert(tk.END,
                                     f"{food.name} (pref:{food.prefered_count})")

    def add_food_button(self):
        food_name = self.food_entry.get().strip()
        if not food_name:
            messagebox.showwarning("Warning", "Please enter a food name.")
            return
        similars = food_app.search_similar_foods(food_name)
        if similars:
            result = messagebox.askyesno(
                "Save",
                f"{similars} are currently in the database. Do you want to add this one as well?"
            )
            if result:
                self.foodapp.add_food(food_name)
                self.window.refresh_combo_food()
                self.refresh_food_list()
        else:
            self.foodapp.add_food(food_name)
            self.window.refresh_combo_food()
            self.refresh_food_list()
        self.food_entry.delete(0, tk.END)


class MealTemplate(tk.Frame):
    def __init__(self, parent, foodapp=food_app):
        super().__init__(master=parent, bg="green")
        self.foodapp = foodapp

        # --- فرم افزودن وعده ---
        self.meal_label = tk.Label(self, text="meal name", bg="green")
        self.meal_label.pack(pady=(10, 0))

        self.food_var = tk.StringVar()
        self.food_combo = ttk.Combobox(self, textvariable=self.food_var,
                                       values=self.foodapp.collect_food_name(),
                                       state="readonly")
        self.food_combo.pack(pady=5)

        self.date_label = tk.Label(self, text="date (YYYY-MM-DD)", bg="green")
        self.date_label.pack()
        self.date_entry = tk.Entry(self)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.pack()

        self.meal_add_button = FoodAppButton(master=self, text="add meal",
                                             command=self.add_meal_button)
        self.meal_add_button.pack(pady=5)

        # --- لیست وعده‌ها ---
        self.meal_list_label = tk.Label(self, text="Meal List", bg="green",
                                        font=("Arial", 10, "bold"))
        self.meal_list_label.pack(pady=(15, 0))
        self.meal_listbox = tk.Listbox(self, height=15, width=30)
        self.meal_listbox.pack(pady=5, padx=10, fill="both", expand=True)

        self.refresh_meal_list()

    def refresh_meal_list(self):
        self.meal_listbox.delete(0, tk.END)
        for meal in self.foodapp.fetch_meal():
            self.meal_listbox.insert(tk.END, f"{meal.food} - {meal.date}")

    def add_meal_button(self):
        food_name = self.food_var.get().strip()
        date_str = self.date_entry.get().strip()

        if not food_name:
            messagebox.showwarning("Warning", "Please select a food.")
            return
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Warning", "Date format must be YYYY-MM-DD.")
            return

        meal_str = f"{food_name},{date_str}"
        self.foodapp.add_meal(meal_str)
        self.refresh_meal_list()
        self.food_var.set("")


class ChartTemplate(tk.Frame):
    def __init__(self, parent, foodapp=food_app):
        super().__init__(master=parent, bg="red")
        self.foodapp = foodapp

        self.chart_label = tk.Label(self, text="Chart - Food Preference",
                                    bg="red", font=("Arial", 12, "bold"))
        self.chart_label.pack(pady=10)

        self.canvas = tk.Canvas(self, bg="white", height=250)
        self.canvas.pack(fill="both", expand=True, padx=20, pady=10)

        self.refresh_button = FoodAppButton(master=self, text="refresh",
                                            command=self.draw_chart)
        self.refresh_button.pack(pady=5)

        self.draw_chart()

    def draw_chart(self):
        self.canvas.delete("all")
        foods = self.foodapp.fetch_food()
        if not foods:
            self.canvas.create_text(200, 100, text="No data available",
                                    fill="gray")
            return

        max_count = max(f.prefered_count for f in foods) or 1
        bar_width = 40
        gap = 20
        x = 40
        base_y = 220

        for food in foods:
            height = (food.prefered_count / max_count) * 180
            self.canvas.create_rectangle(x, base_y - height,
                                         x + bar_width, base_y,
                                         fill="steelblue")
            self.canvas.create_text(x + bar_width / 2, base_y - height - 10,
                                    text=str(food.prefered_count))
            self.canvas.create_text(x + bar_width / 2, base_y + 10,
                                    text=food.name, angle=45)
            x += bar_width + gap


class SuggestionTemplate(tk.Frame):
    def __init__(self, parent, foodapp=food_app):
        super().__init__(master=parent, bg="lightblue")
        self.foodapp = foodapp

        self.suggestion_label = tk.Label(self, text="Suggestions",
                                         bg="lightblue",
                                         font=("Arial", 12, "bold"))
        self.suggestion_label.pack(pady=10)

        self.suggestion_listbox = tk.Listbox(self, height=15, width=30)
        self.suggestion_listbox.pack(pady=5, padx=10, fill="both", expand=True)

        self.refresh_button = FoodAppButton(master=self, text="suggest",
                                            command=self.generate_suggestions)
        self.refresh_button.pack(pady=5)

        self.generate_suggestions()

    def generate_suggestions(self):
        self.suggestion_listbox.delete(0, tk.END)
        foods = self.foodapp.fetch_food()
        if not foods:
            self.suggestion_listbox.insert(tk.END, "No foods available.")
            return

        sorted_foods = sorted(foods, key=lambda f: (f.month_cook, f.week_cook))
        for food in sorted_foods[:10]:
            self.suggestion_listbox.insert(
                tk.END,
                f"{food.name} (month:{food.month_cook}, week:{food.week_cook})"
            )


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("main_page")
        self.geometry("1200x800")
        self.resizable(width=False, height=False)

        self.food_frame = FoodTemplate(parent=self, window=self)
        self.food_frame.grid(row=1, column=0, sticky="nsew")
        self.meal_frame = MealTemplate(self)
        self.meal_frame.grid(row=1, column=1, sticky="nsew")
        self.chart_frame = ChartTemplate(self)
        self.chart_frame.grid(row=0, column=0, sticky="nsew", columnspan=3)
        self.suggestion_frame = SuggestionTemplate(self)
        self.suggestion_frame.grid(row=1, column=2, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=2)

    def refresh_combo_food(self):
        self.meal_frame.food_combo["values"] = food_app.collect_food_name()

    def run(self):
        self.mainloop()


def main():
    main_window = Window()
    main_window.run()


if __name__ == "__main__":
    main()