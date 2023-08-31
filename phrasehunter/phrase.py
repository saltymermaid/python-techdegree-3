class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()


    def display(self, guesses):
        display_string = ''
        for letter in self.phrase:
            if letter in guesses:
                display_string += letter
            elif letter == " ":
                display_string += " "
            else:
                display_string += '_'
            display_string += ' '
        print(display_string)


    def check_letter(self, guess):
        return guess in self.phrase


    def check_complete(self, guesses):
        letters_in_phrase = set(self.phrase.replace(" ", ""))
        guessed_letters = set(guesses)
        return letters_in_phrase.difference(guessed_letters) == set()