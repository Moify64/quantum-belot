from components.enums import CardRank, CardSuit
from ecs.entity_manager import EntityManager
from card_engine.components import CardComponent, ZoneComponent
from components.card_info import CardInfo
from components.superposition import Superposition

def generate_base_deck(em: EntityManager):
    cards = []
    
    for rank in CardRank:
        for suit in CardSuit:
            card = em.create_entity()
            em.add_component(card, CardInfo(rank=rank, suit=suit))
            em.add_component(card, CardComponent(name=f"{rank.name} of {suit.name}"))
            em.add_component(card, Superposition())
            cards.append(str(card))

    deck_id = em.create_entity()
    em.add_component(deck_id, ZoneComponent(name="Deck", cards=cards))
    return deck_id
