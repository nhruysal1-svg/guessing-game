from number import Number
from result import Result


class Game:
    def play(self):
        number = Number().generate()

        guess = int(input("Guess number: "))

        result = Result()

        print(result.check(guess, number))


game = Game()
game.play()
