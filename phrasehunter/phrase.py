class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()


    def display(self, guesses):
        display_string = ''
        for letter in self.phrase:
            if letter in guesses:
                display_string += letter
            else:
                display_string += '_'
            display_string += ' '
        print(display_string)


    def check_letter(self):
        print("Letter checked")


    def check_complete(self):
        pass