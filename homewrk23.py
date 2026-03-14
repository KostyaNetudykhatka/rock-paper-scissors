import tkinter as tk
import random

choices = ["Камінь", "Ножиці", "Папір"]

def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "Нічия!"
    elif (user_choice == "Камінь" and computer_choice == "Ножиці") or \
         (user_choice == "Ножиці" and computer_choice == "Папір") or \
         (user_choice == "Папір" and computer_choice == "Камінь"):
        result = "Ти виграв!"
    else:
        result = "Комп'ютер виграв!"

    label_result.config(text=f"Ти: {user_choice}\nКомп'ютер: {computer_choice}\n{result}")

window = tk.Tk()
window.title("Камінь Ножиці Папір")
window.geometry("300x250")

label_title = tk.Label(window, text="Оберіть варіант", font=("Arial", 14))
label_title.pack(pady=10)

btn_rock = tk.Button(window, text="Камінь", width=15, command=lambda: play("Камінь"))
btn_rock.pack(pady=5)

btn_scissors = tk.Button(window, text="Ножиці", width=15, command=lambda: play("Ножиці"))
btn_scissors.pack(pady=5)

btn_paper = tk.Button(window, text="Папір", width=15, command=lambda: play("Папір"))
btn_paper.pack(pady=5)

label_result = tk.Label(window, text="", font=("Arial", 12))
label_result.pack(pady=15)

window.mainloop()