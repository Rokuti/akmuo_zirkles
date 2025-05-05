import csv
import os

FILE = "data/history.csv"

def save_result(user, user_choice, computer_choice, result):
    os.makedirs("data", exist_ok=True)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([user, user_choice, computer_choice, result])
