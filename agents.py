from dataStructs import Stack
from abc import ABC, abstractmethod
from logic import action, result, terminal

# this is just going to be used for the purpose ofcreating subclasses
class Agent(ABC):
    def __init__(self, max: str):
        self.max = max
        self.min = "O" if max == "X" else "X"

    @abstractmethod
    def get_move(self, state: list) -> tuple:
        pass

class MinimaxAgent(Agent):
    