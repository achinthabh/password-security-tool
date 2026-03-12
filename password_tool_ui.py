import tkinter as tk
from tkinter import messagebox
import hashlib
import re

# -----------------------------
# Password Strength Function
# -----------------------------
def check_strength():

    password = password_entry.get()

    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&*!]", password):
        score += 1

    if score <= 2:
        result = "Weak Password ❌"
    elif score <= 4:
        result = "Medium Password ⚠️"
    else:
        result = "Strong Password ✅"

    result_label.config(text=result)


# -----------------------------
# Hash Generator
# -----------------------------
def generate_hash():

    password = password_entry.get()

    hashed = hashlib.sha256(password.encode()).hexdigest()

    hash_label.config(text=hashed)


# -----------------------------
# Dictionary Attack
# -----------------------------
def dictionary_attack():

    target_hash = hash_entry.get()

    try:
        wordlist = open("wordlist.txt","r")
    except:
        messagebox.showerror("Error","wordlist.txt not found")
        return

    for word in wordlist:

        word = word.strip()

        hashed_word = hashlib.sha256(word.encode()).hexdigest()

        if hashed_word == target_hash:

            messagebox.showinfo("Success", f"Password Found: {word}")
            return

    messagebox.showinfo("Result","Password not found in wordlist")


# -----------------------------
# UI Window
# -----------------------------
window = tk.Tk()
window.title("Password Security Tool 🔐")
window.geometry("500x400")

# Password input
tk.Label(window, text="Enter Password").pack()

password_entry = tk.Entry(window, width=40)
password_entry.pack()

tk.Button(window, text="Check Strength", command=check_strength).pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack()

tk.Button(window, text="Generate SHA256 Hash", command=generate_hash).pack(pady=5)

hash_label = tk.Label(window, text="")
hash_label.pack()

# Hash input for cracking
tk.Label(window, text="Enter Hash to Crack").pack(pady=10)

hash_entry = tk.Entry(window, width=40)
hash_entry.pack()

tk.Button(window, text="Dictionary Attack", command=dictionary_attack).pack(pady=10)

window.mainloop()
