import tkinter as tk
from logic import get_computer_choice, determine_winner
from storage import save_result
from stats import get_statistics

class RPSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Akmuo, popierius, žirklės")

        self.username = None

        self.login_frame = tk.Frame(root)
        tk.Label(self.login_frame, text="Įveskite vartotojo vardą:").pack(pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(pady=5)
        tk.Button(self.login_frame, text="Pradėti", command=self.start_game).pack(pady=5)
        self.login_frame.pack()

    def start_game(self):
        name = self.username_entry.get().strip()
        if not name:
            return
        self.username = name
        self.login_frame.pack_forget()
        self.build_game_ui()

    def build_game_ui(self):
        tk.Label(self.root, text=f"Sveiki, {self.username}!", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Pasirink savo ėjimą:", font=("Arial", 12)).pack()

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=5)

        for choice in ["akmuo", "popierius", "žirklės"]:
            tk.Button(self.buttons_frame, text=choice.title(), width=12, command=lambda c=choice: self.play(c)).pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.stats_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.stats_label.pack()
        self.update_stats()

    def play(self, user_choice):
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        save_result(self.username, user_choice, computer_choice, result)

        self.result_label.config(
            text=f"Tu: {user_choice} | Kompiuteris: {computer_choice} → {result}"
        )
        self.update_stats()

    def update_stats(self):
        stats = get_statistics(self.username)
        self.stats_label.config(
            text=f"Laimėjimai: {stats['win']}  |  Pralaimėjimai: {stats['lose']}  |  Lygiosios: {stats['draw']}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSApp(root)
    root.mainloop()
