import pytest
from card_engine.components import ZoneComponent, CardComponent
from card_engine.systems import move_card, draw_card, shuffle_zone, move_card_to_index

@pytest.fixture
def setup_for_tests():
    # Create two zones
    zone1 = ZoneComponent(name="Deck", cards=["card_0", "card_1", "card_2"])
    zone2 = ZoneComponent(name="Hand", cards=[])
    
    # We don't strictly need CardComponent instances for systems since they only care about IDs
    # but they are good for representing the "entities"
    cards = [
        CardComponent(name="Card 0"),
        CardComponent(name="Card 1"),
        CardComponent(name="Card 2")
    ]
    
    return zone1, zone2, ["card_0", "card_1", "card_2"]

def test_move_card(setup_for_tests):
    zone1, zone2, card_ids = setup_for_tests
    card_to_move = card_ids[0]
    
    move_card(card_to_move, zone1, zone2)
    
    assert card_to_move not in zone1.cards
    assert card_to_move in zone2.cards
    assert len(zone1.cards) == 2
    assert len(zone2.cards) == 1

def test_move_card_invalid_card(setup_for_tests):
    zone1, zone2, card_ids = setup_for_tests
    with pytest.raises(ValueError, match="Card InvalidID not in zone Deck"):
        move_card("InvalidID", zone1, zone2)

def test_move_card_not_in_zone(setup_for_tests):
    zone1, zone2, card_ids = setup_for_tests
    with pytest.raises(ValueError, match=f"Card {card_ids[0]} not in zone Hand"):
        move_card(card_ids[0], zone2, zone1)

def test_draw_card(setup_for_tests):
    zone1, zone2, card_ids = setup_for_tests
    top_card = card_ids[-1]
    
    drawn_card_id = draw_card(zone1, zone2)
    
    assert drawn_card_id == top_card
    assert top_card not in zone1.cards
    assert top_card in zone2.cards

def test_draw_card_empty():
    zone1 = ZoneComponent(name="Empty", cards=[])
    zone2 = ZoneComponent(name="Hand", cards=[])
    
    drawn_card_id = draw_card(zone1, zone2)
    assert drawn_card_id is None

def test_shuffle_zone(setup_for_tests):
    zone1, _, card_ids = setup_for_tests
    original_order = list(zone1.cards)
    
    # Try up to 6 times to get a different order (probabilistic)
    is_shuffled = False
    for _ in range(6):
        shuffle_zone(zone1)
        if zone1.cards != original_order:
            is_shuffled = True
            break
            
    assert is_shuffled, "Zone order did not change after 6 shuffles"
    assert len(zone1.cards) == len(original_order)
    assert set(zone1.cards) == set(original_order)

def test_move_card_to_index(setup_for_tests):
    zone1, zone2, card_ids = setup_for_tests
    card_to_move = card_ids[0] # Card 0
    
    # Move Card 0 to index 0 of zone 2 (which is empty)
    move_card_to_index(card_to_move, zone1, zone2, 0)
    
    assert zone2.cards[0] == card_to_move

def test_move_card_to_index_same_zone(setup_for_tests):
    zone1, _, card_ids = setup_for_tests
    # Initial: [C0, C1, C2]
    assert zone1.cards == ["card_0", "card_1", "card_2"]
    
    # Move C0 to index 2
    # Step 1: Remove C0 -> [C1, C2]
    # Step 2: Insert C0 at index 2 -> [C1, C2, C0]
    move_card_to_index("card_0", zone1, zone1, 2)
    assert zone1.cards == ["card_1", "card_2", "card_0"]
    
    # Move C2 to index 0
    # Step 1: Remove C2 -> [C1, C0]
    # Step 2: Insert C2 at index 0 -> [C2, C1, C0]
    move_card_to_index("card_2", zone1, zone1, 0)
    assert zone1.cards == ["card_2", "card_1", "card_0"]

def test_move_card_to_index_out_of_bounds(setup_for_tests):
    zone1, zone2, card_ids = setup_for_tests
    with pytest.raises(ValueError, match="Index out of bounds"):
        move_card_to_index("card_0", zone1, zone2, 5)
