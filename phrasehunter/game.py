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
DISPLAY_WIDTH = 60

FLAG = """
888888888888888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888P""  ""9888888888888888888888888888
8888888888888888P"88888P          988888"9888888888888888888
8888888888888888  "9888            888P"  888888888888888888
888888888888888888bo "9  d8o  o8b  P" od88888888888888888888
888888888888888888888bob 98"  "8P dod88888888888888888888888
888888888888888888888888    db    88888888888888888888888888
88888888888888888888888888      8888888888888888888888888888
88888888888888888888888P"9bo  odP"98888888888888888888888888
88888888888888888888P" od88888888bo "98888888888888888888888
888888888888888888   d88888888888888b   88888888888888888888
8888888888888888888oo8888888888888888oo888888888888888888888
888888888888888888888888888888888888888888888888888888888888
"""

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = Game.make_phrases()
        self.active_phrase = None
        self.guesses = []


    def make_phrases():
        """Create a list of phrases"""
        phrases = []
        for phrase in PHRASES:
            phrases.append(Phrase(phrase))
        return phrases


    def start(self):
        """Start the game"""
        Game.welcome()
        self.get_random_phrase()
        phrase = self.active_phrase
        guesses = self.guesses
        phrase.display(guesses)
        while not self.game_over():
            guess = self.get_guess()
            correct = phrase.check_letter(guess)
            if not correct:
                print("Arr, not quite!")
                self.missed += 1
            else:
                print("Yar, ye got it!")
            print(f"Ye've got {self.missed} blunders an' still have {NUM_GUESSES - self.missed} chances left, arr!")
            phrase.display(guesses)


    def get_random_phrase(self):
        """Get a random phrase from the phrases list"""
        self.active_phrase = random.choice(self.phrases)
        pass


    def welcome():
        """Display welcome message"""
        print('*' * DISPLAY_WIDTH)
        print("*" + ' ' * (DISPLAY_WIDTH - 2) + "*")
        print("* " + "Ahoy, welcome to Phrase Huntin', ye scallywag!!!".center(DISPLAY_WIDTH - 4, ' ') + " *")
        print("* " + f"Ye be havin' {NUM_GUESSES} shots to suss out th' sayin'.".center(DISPLAY_WIDTH - 4, ' ') + " *")
        print("*" + ' ' * (DISPLAY_WIDTH - 2) + "*")
        print('*' * DISPLAY_WIDTH)


    def get_guess(self):
        """Get a valid guess from the user"""
        valid = False
        while not valid:
            guessed_letter = input("\nPick yar letter, if ye please > ").lower()
            if len(guessed_letter) == 1 and guessed_letter.isalpha():
                print()
                if guessed_letter in self.guesses:
                    print(f"Yar, ye've already wagered on {guessed_letter}, matey.")
                else:
                    valid = True
        self.guesses.append(guessed_letter)
        return guessed_letter


    def game_over(self):
        """Check if the game should end"""
        solved = self.active_phrase.check_complete(self.guesses)
        if self.missed < 5 and not solved:
            return False
        elif solved:
            print("Shiver me timbers, ye've got th' phrase!!")
        else:
            print(FLAG)
            print(f"Yar out o' chances. Th' phrase be: ")
            self.active_phrase.display(set(self.active_phrase.phrase))
        self.play_again()
        return True


    def play_again(self):
        """Ask the user if they want to play again"""
        go_again = input("Wish to sail these seas once more? Y/N > ").lower()
        if go_again == 'y':
            self.reset_game()
        else:
            print("Me thanks fer joinin' th' game, ye hearty!!")


    def reset_game(self):
        """Reset the game"""
        self.missed = 0
        self.active_phrase = None
        self.guesses = []
        self.start()