import enum

from ecs.component import Component
from components.enums import CardRank, CardSuit

class CardInfo(Component):
    
    def __init__(self, rank: CardRank, suit: CardSuit):
        self.rank = rank
        self.suit = suit