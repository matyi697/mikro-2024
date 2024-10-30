import pandas as pd
import tkinter as tk
from tkinter import messagebox
import random

file_path = 'kerdesek.xlsx'  
data = pd.read_excel(file_path)

unflagged_data = data[data.iloc[:, 2].isna() | (data.iloc[:, 2] != 'tudom')]
questions = unflagged_data.sample(frac=1).reset_index(drop=True)
current_index = 0

root = tk.Tk()
root.title("Mikroelektronika")
root.geometry("500x450")

question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
question_label.pack(pady=20)

answer_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12), fg="gray")
answer_label.pack(pady=10)

def show_question():
    global current_index
    question = questions.iloc[current_index, 0]
    question_label.config(text=question)
    answer_label.config(text="")

def show_answer():
    answer = questions.iloc[current_index, 1]
    answer_label.config(text=answer)

def next_question():
    global current_index
    if current_index < len(questions) - 1:
        current_index += 1
        show_question()
    else:
        messagebox.showinfo("Skibidi", "Grat, kivitted  mikro targyat, hivatalosan is IMSC hallgato vagy")
        root.quit()

def flag_know():
    global current_index
    questions.iloc[current_index, 2] = 'tudom'
    save_to_excel()
    next_question()

def flag_dont_know():
    global current_index
    questions.iloc[current_index, 2] = 'nem tudom'
    save_to_excel()
    next_question()

def save_to_excel():
    data.update(questions[[data.columns[0], data.columns[1], 'Flag']])
    data.to_excel(file_path, index=False)

show_answer_button = tk.Button(root, text="Válasz megjelenítése", command=show_answer)
show_answer_button.pack(pady=5)

next_question_button = tk.Button(root, text="Következő kérdés", command=next_question)
next_question_button.pack(pady=5)

know_button = tk.Button(root, text="Tudom", command=flag_know)
know_button.pack(pady=5)

dont_know_button = tk.Button(root, text="Nem tudom", command=flag_dont_know)
dont_know_button.pack(pady=5)

show_question()

root.mainloop()