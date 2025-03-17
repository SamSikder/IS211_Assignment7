import random

class PigGame:
    def __init__(self):
        self.scores = [0, 0]  # Player 1 and Player 2 scores
        self.current_player = 0  # Player 1 starts

    def roll_die(self):
        return random.randint(1, 6)

    def play_turn(self):
        turn_total = 0
        print(f"\n{self.get_player_name()} starts their turn.")

        while True:
            roll = self.roll_die()
            print(f"{self.get_player_name()} rolled a {roll}")

            if roll == 1:
                print("Oops! Lost all points this turn.")
                return  # Switch turn

            turn_total += roll
            print(f"Turn total: {turn_total}, Current Score: {self.scores[self.current_player]}")

            decision = input("Roll again (r) or Hold (h)? ").lower()
            if decision == 'h':
                self.scores[self.current_player] += turn_total
                print(f"{self.get_player_name()} holds. New Score: {self.scores[self.current_player]}")
                return  # Switch turn

    def get_player_name(self):
        return f"Player {self.current_player + 1}"

    def play_game(self):
        while max(self.scores) < 100:
            self.play_turn()
            self.current_player = 1 - self.current_player  # Switch player

        print(f"\n🎉 {self.get_player_name()} wins with {max(self.scores)} points! 🎉")

if __name__ == "__main__":
    PigGame().play_game()
