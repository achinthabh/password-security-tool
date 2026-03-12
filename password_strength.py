import re

def check_strength(password):

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
        return "Weak Password ❌"

    elif score == 3 or score == 4:
        return "Medium Password ⚠️"

    else:
        return "Strong Password ✅"


password = input("Enter password: ")

result = check_strength(password)

print("Password Strength:", result)
