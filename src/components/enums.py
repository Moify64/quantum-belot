import enum

class SuperpositionState(enum.IntEnum):
    SUPERPOSITION = 0
    DECLARED = 1
    OBSERVED = 2

class CardSuit(enum.IntEnum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3

class CardRank(enum.IntEnum):
    SEVEN = 0
    EIGHT = 1
    NINE = 2
    TEN = 3
    JACK = 4
    QUEEN = 5
    KING = 6
    ACE = 7