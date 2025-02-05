class ScoreCard:

    def __init__(self, pins):
        self.pins = pins
        self.score = 0

    def __change_to_zero(self):
        return self.pins.replace('-', '0')

    def get_score(self):
        self.pins = self.__change_to_zero()
        for pin in self.pins:
            self.score += int(pin)
        return self.score