import random

def get_computer_choice():
    return random.choice(['akmuo', 'popierius', 'žirklės'])

def determine_winner(user, computer):
    if user == computer:
        return "lygiosios"
    elif (user == "akmuo" and computer == "žirklės") or \
         (user == "popierius" and computer == "akmuo") or \
         (user == "žirklės" and computer == "popierius"):
        return "laimėjai"
    else:
        return "pralaimėjai"

def determine_winner(user, computer):
    if user == computer:
        return "Lygiosios"
    elif (user == "akmuo" and computer == "žirklės") or \
         (user == "popierius" and computer == "akmuo") or \
         (user == "žirklės" and computer == "popierius"):
        return "Laimėjai"
    else:
        return "Pralaimėjai"
