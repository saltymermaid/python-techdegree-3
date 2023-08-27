import random
from phrasehunter.phrase import Phrase

PHRASES = [
    "Treasure Map",
    "Jolly Roger",
    "Sea Witch",
    "Siren Song",
    "Walk the Plank"
]
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
        in_progress = True
        self.active_phrase.display(self.guesses)
        while in_progress:
            self.get_guess()
            self.active_phrase.check_letter()
            self.active_phrase.display(self.guesses)
            in_progress = False


    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrases)
        pass


    def welcome():
        print("Welcome to Phrase Hunter!!!")


    def get_guess(self):
        invalid = True
        while invalid:
            guessed_letter = input("Please choose a letter > ")
            invalid = False
        self.guesses.append(guessed_letter)


    def game_over(self):
        pass