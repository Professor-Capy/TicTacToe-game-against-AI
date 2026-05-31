from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, player_symbol: str):
        self.player_symbol = player_symbol
        self.opponent_symbol = "O" if player_symbol == "X" else "X"

    @abstractmethod
    def get_move(self, state: list) -> tuple:
        pass
