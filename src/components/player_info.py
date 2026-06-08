from typing import Dict
from card_engine.components import ZoneComponent
from ecs.component import Component

class PlayerInfo(Component):
    
    def __init__(self, name: str, hand: ZoneComponent, other_players_hands: Dict[str, ZoneComponent]):
        self.name = name
        self.hand = hand
        self.other_players_hands = other_players_hands