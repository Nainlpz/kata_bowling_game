class ScoreCard:

    def __init__(self, pins):
        self.pins = pins
        self.score = 0

    def get_score(self):
        for pin in self.pins:
            self.score += int(pin)
        return self.score