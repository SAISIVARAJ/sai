import random

class WordGuessGame:
    def __init__(self, word_list=None):
        """Initialize the game with a list of words or a default list."""
        self.word_list = word_list or ["python", "framework", "developer", "engineer", "automation"]
        self.target_word = ""
        self.guessed_word = ""
        self.attempts = 0
        self.max_attempts = 10

    def load_words_from_file(self, file_path):
        """Load words from a text file (one word per line)."""
        try:
            with open(file_path, "r") as file:
                self.word_list = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("File not found. Using default word list.")

    def select_random_word(self):
        """Select a random word from the list."""
        self.target_word = random.choice(self.word_list).lower()
        self.guessed_word = "_" * len(self.target_word)

    def display_status(self):
        """Display the current guessed word and attempts left."""
        print(f"\nGuessed Word: {self.guessed_word}")
        print(f"Attempts Left: {self.max_attempts - self.attempts}")

    def update_guessed_word(self, letter):
        """Update the guessed word based on the player's input."""
        new_guessed_word = list(self.guessed_word)
        for idx, char in enumerate(self.target_word):
            if char == letter:
                new_guessed_word[idx] = letter
        self.guessed_word = "".join(new_guessed_word)

    def play_turn(self, letter):
        """Process a single turn of the game."""
        if letter in self.target_word:
            self.update_guessed_word(letter)
            print(f"Good guess! '{letter}' is in the word.")
        else:
            self.attempts += 1
            print(f"Wrong guess. '{letter}' is not in the word.")

    def check_game_over(self):
        """Check if the game is over."""
        if self.guessed_word == self.target_word:
            print(f"\nCongratulations! You've guessed the word: {self.target_word}")
            return True
        if self.attempts >= self.max_attempts:
            print(f"\nGame Over. The word was: {self.target_word}")
            return True
        return False

    def start_game(self):
        """Start the word guessing game."""
        self.select_random_word()
        print("Welcome to the Word Guessing Game!")
        while not self.check_game_over():
            self.display_status()
            guess = input("Enter a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                self.play_turn(guess)
            else:
                print("Invalid input. Please enter a single letter.")
        print("Thanks for playing!")

# Example usage
if __name__ == "__main__":
    game = WordGuessGame()
    game.start_game()
