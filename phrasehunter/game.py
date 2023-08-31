import random
from phrasehunter.phrase import Phrase

PHRASES = [
    "Treasure Map",
    "Jolly Roger",
    "Sea Witch",
    "Siren Song",
    "Walk the Plank",
    "Shipwreck Cove",
    "Coral Reef",
    "Pirate Queen",
    "Davy Jones",
    "Mermaid Tail",
    "Ghost Ship",
    "Nautical Star",
    "Black Pearl",
    "Salty Sailor",
    "Hidden Cove",
    "Anchors Aweigh"
]

NUM_GUESSES = 5

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = Game.make_phrases()
        self.active_phrase = None
        self.guesses = []


    def make_phrases():
        phrases = []
        for phrase in PHRASES:
            phrases.append(Phrase(phrase))
        return phrases


    def start(self):
        Game.welcome()
        self.get_random_phrase()
        phrase = self.active_phrase
        guesses = self.guesses
        in_progress = True
        # show the phrase before guessing starts
        phrase.display(guesses)
        while in_progress:
            guess = self.get_guess()
            correct = phrase.check_letter(guess)
            if not correct:
                self.missed += 1
            print(f"You have {NUM_GUESSES - self.missed} remaining misses.")
            phrase.display(guesses)
            in_progress = self.game_should_continue()


    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrases)
        pass


    def welcome():
        print("Welcome to Phrase Hunter!!!")


    def get_guess(self):
        valid = False
        while not valid:
            guessed_letter = input("Please choose a letter > ").lower()
            if len(guessed_letter) == 1 and guessed_letter.isalpha():
                if guessed_letter in self.guesses:
                    print(f"You've already guessed {guessed_letter}.")
                else:
                    valid = True
        self.guesses.append(guessed_letter)
        return guessed_letter


    def game_should_continue(self):
        solved = self.active_phrase.check_complete(self.guesses)
        if self.missed < 5 and not solved:
            return True
        elif solved:
            print("You got it!!")
        else:
            print(f"You're out of guesses. The phrase is: ")
            self.active_phrase.display(set(self.active_phrase.phrase))
        self.game_over()
        return False


    def game_over(self):
        go_again = input("Do you want to play again? Y/N > ").lower()
        if go_again == 'y':
            self.reset_game()
        else:
            print("Thank you for playing!!")


    def reset_game(self):
        self.missed = 0
        self.active_phrase = None
        self.guesses = []
        self.start()