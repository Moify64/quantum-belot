
import enum

from ecs.component import Component
from components.enums import SuperpositionState

class Superposition(Component):
    
    def __init__(self):
        self.state = SuperpositionState.SUPERPOSITION

