from typing import Set, List, Dict, Type, TypeVar, Optional

T = TypeVar('T', bound='Component')

class EntityManager:
    """
    Manages the lifecycle of entities and their associated components.
    Entities are represented by unique integer IDs.
    """
    def __init__(self):
        self._next_entity_id: int = 0
        self._entities: Set[int] = set()
        self._reusable_ids: List[int] = []
        # Map of component type -> entity_id -> component_instance
        self._components: Dict[Type, Dict[int, any]] = {}

    def create_entity(self) -> int:
        """
        Creates a new entity and returns its unique ID.
        Reuses IDs from destroyed entities if available.
        """
        if self._reusable_ids:
            entity_id = self._reusable_ids.pop()
        else:
            entity_id = self._next_entity_id
            self._next_entity_id += 1
        
        self._entities.add(entity_id)
        return entity_id

    def destroy_entity(self, entity_id: int) -> None:
        """
        Destroys an entity and all its associated components.
        Makes its ID available for reuse.
        """
        if entity_id in self._entities:
            # Remove all components associated with this entity
            for component_type in self._components:
                self._components[component_type].pop(entity_id, None)
            
            self._entities.remove(entity_id)
            self._reusable_ids.append(entity_id)

    def add_component(self, entity_id: int, component: any) -> None:
        """
        Adds a component to an entity.
        """
        if not self.is_alive(entity_id):
            raise ValueError(f"Entity {entity_id} does not exist.")
        
        component_type = type(component)
        if component_type not in self._components:
            self._components[component_type] = {}
        
        self._components[component_type][entity_id] = component

    def get_component(self, entity_id: int, component_type: Type[T]) -> Optional[T]:
        """
        Gets a component of a specific type for an entity.
        """
        return self._components.get(component_type, {}).get(entity_id)

    def has_component(self, entity_id: int, component_type: Type) -> bool:
        """
        Checks if an entity has a specific component type.
        """
        return entity_id in self._components.get(component_type, {})

    def remove_component(self, entity_id: int, component_type: Type) -> None:
        """
        Removes a component from an entity.
        """
        if component_type in self._components:
            self._components[component_type].pop(entity_id, None)

    def get_entities_with_components(self, *component_types: Type) -> Set[int]:
        """
        Returns a set of entity IDs that have all the specified component types.
        """
        if not component_types:
            return self.active_entities
        
        sets = [set(self._components.get(ct, {}).keys()) for ct in component_types]
        return set.intersection(*sets) if sets else set()

    def is_alive(self, entity_id: int) -> bool:
        """
        Checks if an entity exists.
        """
        return entity_id in self._entities

    @property
    def active_entities(self) -> Set[int]:
        """
        Returns a set of all currently active entity IDs.
        """
        return self._entities.copy()
