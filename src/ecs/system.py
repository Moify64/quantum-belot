from abc import ABC, abstractmethod

class System(ABC):
    """
    Base class for all systems.
    Systems contain logic that operates on entities with specific components.
    """
    @abstractmethod
    def update(self, dt: float, entity_manager, *args, **kwargs):
        """
        Process the entities.
        """
        pass
