from card_engine.systems import shuffle_zone
from ecs.entity_manager import EntityManager
from ecs.component import Component
from ecs.system import System
from systems.basedeck import generate_base_deck



def main():
    manager = EntityManager()
    basedeck = generate_base_deck(manager)
    shuffle_zone(basedeck.get_component("ZoneComponent").cards)
    # Create an entity
    player = manager.create_entity()
    
    # Create another entity
    npc = manager.create_entity()
    manager.add_component(npc, Position(10, 10))
    # NPC doesn't have velocity, so it won't move
    
    # Run the movement system
    move_system = MovementSystem()
    
    print("Initial State:")
    for entity in manager.active_entities:
        pos = manager.get_component(entity, Position)
        print(f"Entity {entity} at ({pos.x}, {pos.y})")
    
    print("\nUpdating Movement System (dt=1.0)...")
    move_system.update(1.0, manager)
    
    print("\nDestroying Player Entity...")
    manager.destroy_entity(player)
    print(f"Is Player alive? {manager.is_alive(player)}")
    print(f"Active entities: {manager.active_entities}")

if __name__ == "__main__":
    main()
