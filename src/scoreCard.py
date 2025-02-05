class ScoreCard:

    MAX_PINS = 10

    def __init__(self, pins):
        self.pins = pins
        self.score = 0

    def __change_to_zero(self):
        return self.pins.replace('-', '0')
    
    def __calculate_spare(self):
        pins = self.__change_to_zero()
        for position in range(len(pins)):
            if pins[position] == '/':
                self.score += ScoreCard.MAX_PINS - int(pins[position - 1]) + int(pins[position + 1])
        self.pins = pins.replace('/', '')
        return self.score

    def get_score(self):
        self.pins = self.__change_to_zero()
        self.score = self.__calculate_spare()
        for pin in self.pins:
            self.score += int(pin)
        return self.score