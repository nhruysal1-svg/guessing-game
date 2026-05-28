class Result:
    def check(self, guess, number):
        if guess == number:
            return "Correct!"

        return "Wrong!"
