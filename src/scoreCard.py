class ScoreCard:

    MAX_PINS = 10

    def __init__(self, pins):
        self.pins = list(pins)
        self.score = 0

    def __change_to_zero(self):
        self.pins = [0 if pin == "-" else pin for pin in self.pins]
        return self.pins
    
    def __calculate_spare(self):
        self.pins = self.__change_to_zero()
        position = 0
        while position < len(self.pins) - 1:
            if self.pins[position] == '/':
                self.pins[position] = ScoreCard.MAX_PINS - int(self.pins[position - 1]) + int(self.pins[position + 1])
            position += 1
        return self.pins
    
    def __calculate_strike(self):
        self.pins = self.__change_to_zero()
        self.pins = ['10' if pin == "X" else pin for pin in self.pins]
        position = 0
        while position < len(self.pins) - 1:
            if self.pins[position] == '10':
                self.pins[position] = ScoreCard.MAX_PINS + int(self.pins[position + 1]) + int(self.pins[position + 2])
            position += 1
        if len(self.pins) > 20:
            return self.pins[:20]
        return self.pins

    def get_score(self):
        self.pins = self.__change_to_zero() and self.__calculate_spare() and self.__calculate_strike()
        print(self.pins)
        return sum(int(pin) for pin in self.pins)