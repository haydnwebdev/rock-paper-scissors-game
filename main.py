import random
import sys


class Game:
    def __init__(self):
        print(
            """
* Welcome to Rock, Paper, Scissors!
* Choose rock, paper, or scissors to start.
* Play against the computer.")
* Type 'exit' to quit the program.
        """
        )

        print()  # intentionally black line

        self.moves: dict = {
            "rock": "🪨",
            "paper": "📜",
            "scissors": "✂️",
        }

        self.valid_moves: list[str] = list(
            self.moves.keys()
        )  # list containing dict keys

        self.player_score = 0
        self.computer_score = 0

    def play_game(self):
        """Start, and continue playing the game."""
        user_move: str = input("Choose rock, paper or scissors >> ").lower()

        if user_move == "exit":
            print("Thanks for playing!")
            sys.exit()

        if user_move not in self.valid_moves:
            print("Invalid move...")
            return self.play_game()  # calls method to play again

        computer_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, computer_move)
        self.check_move(user_move, computer_move)

    def display_moves(self, user_move: str, computer_move: str):
        """Displays the player and computer moves."""
        print("-" * 12)
        print(f"You: {self.moves[user_move]}")
        print(f"Computer: {self.moves[computer_move]}")
        print("-" * 12)

    def check_move(self, user_move: str, computer_move: str):
        """Checks and validate user and computer moves, increments score."""
        if user_move == computer_move:
            print("It's a tie!")
            self.player_score += 1
            self.computer_score += 1
            self.show_scores()
        elif user_move == "rock" and computer_move == "scissors":
            print("You win!")
            self.player_score += 1
            self.show_scores()
        elif user_move == "scissors" and computer_move == "paper":
            print("You win!")
            self.player_score += 1
            self.show_scores()
        elif user_move == "paper" and computer_move == "rock":
            print("You win!")
            self.player_score += 1
            self.show_scores()
        else:
            print("Computer wins!")
            self.computer_score += 1
            self.show_scores()

    def show_scores(self):
        """Displays user and computer scores."""
        print(f"Player: {self.player_score}\tComputer: {self.computer_score}")


if __name__ == "__main__":
    game = Game()

    while True:
        game.play_game()
