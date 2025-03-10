import pytest
from src.scoreCard import ScoreCard


def test_exist_score_card():
    PINS = "12345123451234512345"
    card = ScoreCard(PINS)
    assert card


def test_hitting_pins_regular():
    # Hitting pins total = 60
    PINS = "12345123451234512345"
    total = 60
    card = ScoreCard(PINS)
    assert card.get_score() == total


def test_symbol_zero():
    # test symbol -
    PINS = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    card = ScoreCard(PINS)
    assert card.get_score() == total

    PINS = "9-3561368153258-7181"
    total = 82
    card = ScoreCard(PINS)
    assert card.get_score() == total


def test_spare_not_extra():
    # test spare not extra
    PINS = "9-3/613/815/-/8-7/8-"
    total = 121
    card = ScoreCard(PINS)
    assert card.get_score() == total


def test_strike():
    # test strike
    PINS = "X9-9-9-9-9-9-9-9-9-"
    total = 100
    card = ScoreCard(PINS)
    assert card.get_score() == total

    PINS = "X9-X9-9-9-9-9-9-9-"
    total = 110
    card = ScoreCard(PINS)
    assert card.get_score() == total


def test_two_strikes():
    # two strikes in a row is a double
    PINS = "XX9-9-9-9-9-9-9-9-"
    total = 120
    card = ScoreCard(PINS)
    assert card.get_score() == total


def test_three_strikes():
    # three strikes in a row is a triple
    PINS = "XXX9-9-9-9-9-9-9-"
    total = 141
    card = ScoreCard(PINS)
    assert card.get_score()== total


def test_one_pin_in_extra_roll():
    # one pin in extra roll
    PINS = "9-3/613/815/-/8-7/8/8"
    total = 131
    card = ScoreCard(PINS)
    assert card.get_score()== total

    PINS = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150
    card = ScoreCard(PINS)
    assert card.get_score()== total


def test_two_strikes_in_extra_rolls():
    # two strikes in extra rolls
    PINS = "9-9-9-9-9-9-9-9-9-XXX"
    total = 111
    card = ScoreCard(PINS)
    assert card.get_score()== total


def test_one_strike_in_extra_roll():
    # one strike in extra roll
    PINS = "8/549-XX5/53639/9/X"
    total = 149
    card = ScoreCard(PINS)
    assert card.get_score()== total


def test_spare_in_extra_roll():
    # spare in extra roll
    PINS = "X5/X5/XX5/--5/X5/"
    total = 175
    card = ScoreCard(PINS)
    assert card.get_score()== total


def test_triple_strike_before_extra_rolls():
    # 12 strikes is a “Thanksgiving Turkey”
    # 2 strikes in extra rolls
    PINS = "XXXXXXXXXXXX"
    total = 300
    card = ScoreCard(PINS)
    assert card.get_score()== total