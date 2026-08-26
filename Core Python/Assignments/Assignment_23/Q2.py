# 2. Build a currency converter application that converts between different currencies. The
# user should be able to enter an amount, select the input currency, select the output
# currency, and see the converted amount.

import tkinter as tk
from tkinter import messagebox

rates = {
    "USD": 1,
    "INR": 83,
    "EUR": 0.92,
    "GBP": 0.79
}

def convert():
    try:
        amount = float(amount_entry.get())
        from_currency = from_var.get()
        to_currency = to_var.get()
        # Convert input currency to USD first
        usd_amount = amount / rates[from_currency]
        # Convert USD to output currency
        result = usd_amount * rates[to_currency]
        result_label.config(
            text=f"{amount} {from_currency} = {result:.2f} {to_currency}"
        )
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x300")
tk.Label(root, text="Enter Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()
tk.Label(root, text="From Currency").pack()
from_var = tk.StringVar(value="USD")
from_menu = tk.OptionMenu(
    root, from_var, "USD", "INR", "EUR", "GBP"
)
from_menu.pack()
tk.Label(root, text="To Currency").pack()
to_var = tk.StringVar(value="INR")
to_menu = tk.OptionMenu(root, to_var, "USD", "INR", "EUR", "GBP")
to_menu.pack()
tk.Button(root, text="Convert", command=convert).pack(pady=20)
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()