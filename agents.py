from dataStructs import Stack
from abc import ABC, abstractmethod
from logic import action, result, terminal
from testStates import emptyState

# this is just going to be used for the purpose ofcreating subclasses
class Agent(ABC):
    def __init__(self, max: str):
        self.max = max
        self.min = "O" if max == "X" else "X"

    @abstractmethod
    def getMove(self, state: list) -> dict:
        pass

class MinimaxAgent(Agent):
    def minimax(self, state: list, maximize: bool) -> int:
        nextMax = not maximize


    def getMove(self, state: list) -> dict:
        actions = action(state)
        bestScore = float('-inf')
        bestMove = None
        for move in actions:
            newState = result(state, move)
            score = self.minimax(state, False)

            if score > bestScore:
                bestScore = score
            



if __name__ == '__main__':
    mm = MinimaxAgent('X')
    mm.getMove(emptyState())
    print()
