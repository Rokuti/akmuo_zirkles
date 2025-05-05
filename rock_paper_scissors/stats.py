import csv
from collections import Counter

FILE = "data/history.csv"

def get_statistics(username):
    counts = Counter()
    try:
        with open(FILE, newline="") as f:
            for row in csv.reader(f):
                if row[0] == username:
                    result = row[3]
                    counts[result] += 1
    except FileNotFoundError:
        pass
    return {
        "win": counts["Laimėjai"],
        "lose": counts["Pralaimėjai"],
        "draw": counts["Lygiosios"]
    }
