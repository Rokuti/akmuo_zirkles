from logic import get_computer_choice, determine_winner
from storage import save_result
from stats import get_statistics

def main():
    print("=== Akmuo, Popierius, Žirklės ===")
    while True:
        print("\nPasirink: [a]kmuo, [p]opierius, [z]irklės arba [q] - išeiti")
        user_choice = input("Tavo pasirinkimas: ").lower()

        if user_choice == 'q':
            print("Ačiū, kad žaidei!")
            break

        choices_map = {'a': 'akmuo', 'p': 'popierius', 'z': 'žirklės'}
        if user_choice not in choices_map:
            print("Neteisingas pasirinkimas.")
            continue

        user = choices_map[user_choice]
        computer = get_computer_choice()
        result = determine_winner(user, computer)

        print(f"Tu: {user} | Kompiuteris: {computer} => Rezultatas: {result}")
        save_result(user, computer, result)

        stats = get_statistics()
        print(f"Laimėjimai: {stats['win']}, Pralaimėjimai: {stats['lose']}, Lygiosios: {stats['draw']}")

if __name__ == "__main__":
    main()
