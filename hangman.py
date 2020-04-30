import random
import string

class Hangman:
    def __init__(self):
        self.word_list = ['python', 'java', 'kotlin', 'javascript']
        self.answer = random.choice(self.word_list)
        self.guessed = list("-" * len(self.answer))
        self.bad_tries = []

    def start(self):
        print("H A N G M A N")


    def display_hints(self):
        print("".join(self.guessed))

    def check_typo(self, user_input):
        alp = string.ascii_lowercase
        if len(user_input) > 1:
            print("You should print a single letter")
            return False
        if user_input not in alp:
            print("It is not an ASCII lowercase letter")
            return False
        return True

    def get_guess(self):
        counter = 8
        while counter > 0:
            print()
            self.display_hints()
            guessed_letter = input("Input a letter: ")
            if not self.check_typo(guessed_letter):
                continue
            if guessed_letter in self.guessed or guessed_letter in self.bad_tries:
                print("You already typed this letter")
                continue
            elif guessed_letter in self.answer:
                for i in range(len(self.answer)):
                    if self.answer[i] == guessed_letter:
                        self.guessed[i] = guessed_letter
            else:
                print("No such letter in the word")
                self.bad_tries.append(guessed_letter)
                counter -= 1

            if "-" not in self.guessed:
                print("You guessed the word!")
                print("You survived!")
                return

        print("You are hanged!")



game = Hangman()
game.start()
while True:
    print()
    user_start = input('Type "play" to play the game, "exit" to quit: ')
    if user_start == 'play':
        game.get_guess()
    else:
        break
