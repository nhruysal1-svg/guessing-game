import random


class Game:
    def play(self):
        number = random.randint(1, 10)

        guess = int(input("Guess number: "))

        if guess == number:
            print("Correct!")
        else:
            print("Wrong!")


game = Game()
game.play()
