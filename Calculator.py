# Isra Tariq 
# Task:23
# Creating a calculator that is simple  for my intership task i.e codesoft intership 
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("My Calculator")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to input numbers
        self.entry = tk.Entry(self.master, width=20, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Buttons for digits 0-9
        digits = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
        row_val = 1
        col_val = 0
        for digit in digits:
            tk.Button(self.master, text=digit, width=5, height=2, command=lambda d=digit: self.update_entry(d)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

        # Buttons for operations
        operations = ['+', '-', '*', '/']
        row_val = 1
        col_val = 3
        for operation in operations:
            tk.Button(self.master, text=operation, width=5, height=2, command=lambda op=operation: self.update_entry(op)).grid(row=row_val, column=col_val)
            row_val += 1

        # Button for equal (=) and clear (C)
        tk.Button(self.master, text='=', width=5, height=2, command=self.calculate).grid(row=5, column=0, columnspan=2)
        tk.Button(self.master, text='C', width=5, height=2, command=self.clear_entry).grid(row=5, column=2, columnspan=2)

    def update_entry(self, value):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text + value)

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def clear_entry(self):
        self.entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
app = Calculator(root)
root.mainloop()
