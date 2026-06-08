from typing import List, Dict
from ecs.entity_manager import EntityManager
from card_engine.components import CardComponent, ZoneComponent
from card_engine.systems import draw_card, shuffle_zone

from components.player_info import PlayerInfo
from components.card_info import CardInfo
from systems.basedeck import generate_base_deck

def run_example():
    manager = EntityManager()
    
    # 1. Create 4 Players and their respective Decks and Hands
    players = []
    player_hands = {} # player_name -> hand_component
    
    for i in range(4):
        player_name = f"Player {i+1}"
        player_id = manager.create_entity()
        
        # Generate a Base Deck for this player (32 cards)
        deck_id = generate_base_deck(manager)
        deck_comp = manager.get_component(deck_id, ZoneComponent)
        deck_comp.name = f"{player_name} Deck"
        
        # Create a Hand for this player
        hand_id = manager.create_entity()
        hand_comp = ZoneComponent(name=f"{player_name} Hand", cards=[])
        manager.add_component(hand_id, hand_comp)
        
        players.append({
            "id": player_id,
            "name": player_name,
            "deck_id": deck_id,
            "hand_id": hand_id,
            "hand_comp": hand_comp
        })
        player_hands[player_name] = hand_comp

    # 2. Add PlayerInfo to each player, linking them to their hand and others' hands
    for p_data in players:
        others_hands = {name: hand for name, hand in player_hands.items() if name != p_data["name"]}
        
        info = PlayerInfo(
            name=p_data["name"],
            hand=p_data["hand_comp"],
            other_players_hands=others_hands
        )
        manager.add_component(p_data["id"], info)

    # 3. Shuffle each player's deck and deal 8 cards to their hand
    print("--- Dealing 8 cards to each player from their own base deck ---")
    for p_data in players:
        deck_comp = manager.get_component(p_data["deck_id"], ZoneComponent)
        hand_comp = p_data["hand_comp"]
        
        shuffle_zone(deck_comp)
        
        for _ in range(8):
            draw_card(deck_comp, hand_comp)
            
        print(f"Dealt 8 cards to {p_data['name']}.")

    # 4. Verify Results
    print("\n--- Final State ---")
    for p_data in players:
        info = manager.get_component(p_data["id"], PlayerInfo)
        deck_comp = manager.get_component(p_data["deck_id"], ZoneComponent)
        
        print(f"{info.name}:")
        print(f"  Deck: {len(deck_comp.cards)} cards remaining.")
        print(f"  Hand: {len(info.hand.cards)} cards.")
        
        # Show first 3 cards in hand with their rank and suit
        hand_details = []
        for card_id_str in info.hand.cards[:3]:
            card_id = int(card_id_str)
            card_info = manager.get_component(card_id, CardInfo)
            hand_details.append(f"{card_info.rank.name} of {card_info.suit.name}")
            
        print(f"  Hand Sample: {', '.join(hand_details)} ...")
        
        # Check if they know about other players
        other_names = ", ".join(info.other_players_hands.keys())
        print(f"  Knowledge of others: {other_names}")

if __name__ == "__main__":
    run_example()
