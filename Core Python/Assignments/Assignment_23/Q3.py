# 3. Design a basic calculator to perform +,-,/,*

import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            result = num1 / num2

        result_label.config(text="Result = " + str(result))

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")


root = tk.Tk()
root.title("Calculator")
root.geometry("300x300")

tk.Label(root, text="First Number").pack()
first_entry = tk.Entry(root)
first_entry.pack()

tk.Label(root, text="Second Number").pack()
second_entry = tk.Entry(root)
second_entry.pack()

tk.Label(root, text="Select Operator").pack()

operator_var = tk.StringVar(value="+")

tk.OptionMenu(
    root,
    operator_var,
    "+", "-", "*", "/"
).pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=20)

result_label = tk.Label(root, text="Result = ")
result_label.pack()

root.mainloop()