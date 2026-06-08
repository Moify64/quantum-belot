import random
from .components import ZoneComponent

def move_card(card_id: str, from_zone: ZoneComponent, to_zone: ZoneComponent):
    """Moves a card from one zone to another."""
    if card_id not in from_zone.cards:
        raise ValueError(f"Card {card_id} not in zone {from_zone.name}")
    
    from_zone.cards.remove(card_id)
    to_zone.cards.append(card_id)

def draw_card(from_zone: ZoneComponent, to_zone: ZoneComponent):
    """Draws the top card (last in list) from one zone and moves it to another."""
    if not from_zone.cards:
        return None # Nothing to draw
        
    card_id = from_zone.cards[-1]
    move_card(card_id, from_zone, to_zone)
    return card_id

def shuffle_zone(zone: ZoneComponent):
    """Shuffles the cards in a zone."""
    random.shuffle(zone.cards)

def move_card_to_index(card_id: str, from_zone: ZoneComponent, to_zone: ZoneComponent, index: int):
    """Puts a card at a specific index in a zone."""
    if card_id not in from_zone.cards:
        raise ValueError(f"Card {card_id} not in zone {from_zone.name}")
    if index < 0 or index > len(to_zone.cards):
        raise ValueError("Index out of bounds")
    
    from_zone.cards.remove(card_id)
    to_zone.cards.insert(index, card_id)
