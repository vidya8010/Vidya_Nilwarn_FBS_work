# 1. Develop a simple login system with a username and password field. Implement user
# authentication, and show a success message if the login is successful, or an error
# message if the login fails.

import tkinter as tk
from tkinter import messagebox

def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid username or password")

root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

tk.Label(root, text="Username").pack()
user_entry = tk.Entry(root)
user_entry.pack()

tk.Label(root, text="Password").pack()
pass_entry = tk.Entry(root, show="*")
pass_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()