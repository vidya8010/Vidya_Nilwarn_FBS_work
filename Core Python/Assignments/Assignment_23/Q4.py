# 4. Quiz Game: Create an interactive quiz game with multiple-choice questions. Display
# questions one at a time and allow the user to select an answer. Provide feedback on
# whether the selected answer is correct or incorrect.


import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "Which language is used for Python programming?",
        "options": ["Python", "Java", "C++", "HTML"],
        "answer": "Python"
    },
    {
        "question": "Which keyword is used to create a function?",
        "options": ["func", "def", "function", "create"],
        "answer": "def"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    }
]

current = 0
score = 0


def next_question():
    global current, score

    selected = answer_var.get()

    if selected == "":
        messagebox.showwarning("Quiz", "Please select an answer")
        return

    if selected == questions[current]["answer"]:
        score += 1
        messagebox.showinfo("Result", "Correct Answer!")
    else:
        messagebox.showerror(
            "Result",
            "Incorrect Answer!\n"
            + "Correct Answer: "
            + questions[current]["answer"]
        )

    current += 1

    if current < len(questions):
        show_question()
    else:
        messagebox.showinfo(
            "Quiz Completed",
            f"Your Score: {score}/{len(questions)}"
        )
        root.destroy()


def show_question():
    question_label.config(
        text=questions[current]["question"]
    )

    answer_var.set("")

    for i in range(4):
        radio_buttons[i].config(
            text=questions[current]["options"][i],
            value=questions[current]["options"][i]
        )


root = tk.Tk()
root.title("Quiz Game")
root.geometry("450x350")

question_label = tk.Label(
    root,
    text="",
    wraplength=400,
    font=("Arial", 14)
)
question_label.pack(pady=20)

answer_var = tk.StringVar()

radio_buttons = []

for i in range(4):
    rb = tk.Radiobutton(
        root,
        text="",
        variable=answer_var,
        value="",
        font=("Arial", 12)
    )
    rb.pack(anchor="w", padx=50)
    radio_buttons.append(rb)

tk.Button(
    root,
    text="Next",
    command=next_question
).pack(pady=30)

show_question()

root.mainloop()