from dataStructs import Stack
from abc import ABC, abstractmethod
from logic import action, result, terminal

# this is just going to be used for the purpose ofcreating subclasses
class Agent(ABC):
    def __init__(self, max: str):
        self.max = max
        self.min = "O" if max == "X" else "X"

    @abstractmethod
    def getMove(self, state: list) -> dict:
        pass

class MinimaxAgent(Agent):
    def moveLoop(self, state: list, actions: tuple):
        for move in actions:
            newState = result(state, move)
            isTerminal, point = terminal(newState)
            if isTerminal:
                self.points[move].append(point)

    def getMove(self, state: list) -> dict:
        actions = action(state)
        self.points = {}
        for move in actions:
            self.points[move] = []
        self.moveLoop(state, actions)

        print(self.points)


if __name__ == '__main__':
    mm = MinimaxAgent('X')
    mm.getMove()
