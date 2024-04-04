import random

# define range and max_attempts
lower_bound = 1
upper_bound = 100
max_attempts = 5

# generate the secret number
class NumberGuessingGame:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.secret_number = random.randint(lower_bound, upper_bound)

    # Get the user's guess
    def get_guess(self):
        while True:
            try:
                guess = int(input(f"Guess a number between {self.lower_bound} and {self.upper_bound}: "))
                if self.lower_bound <= guess <= self.upper_bound:
                    return guess
                else:
                    print("Invalid input. Please enter a number within the specified range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Validate guess
    def check_guess(self, guess):
        if guess == self.secret_number:
            return "Correct"
        elif guess < self.secret_number:
            return "Too low"
        else:
            return "Too high"

    # Track the number of attempts, detect if the game is over
    def play_game(self):
        attempts = 0
        won = False
        
        while attempts < max_attempts:
            attempts += 1
            guess = self.get_guess()
            result = self.check_guess(guess)

            if result == "Correct":
                print(f"Congratulations! You guessed the secret number {self.secret_number} in {attempts} attempts.")
                won = True
                break
            else:
                print(f"{result}. Try again!")

        if not won:
            print(f"Sorry, you ran out of attempts! The secret number is {self.secret_number}.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    game = NumberGuessingGame(lower_bound, upper_bound)
    game.play_game()
