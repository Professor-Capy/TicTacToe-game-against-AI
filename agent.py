from dataStructs import Stack
from abc import ABC, abstractmethod
from logic import action, result, terminal
from testStates import almostTerminalXState

# this is just going to be used for the purpose ofcreating subclasses
class Agent(ABC):
    def __init__(self, max: str):
        self.max = max
        self.min = "O" if max == "X" else "X"

    @abstractmethod
    def getMove(self, state: list) -> dict:
        pass

class MinimaxAgent(Agent):
    def minimax(self, state: list, isMaximize: bool) -> int:
        isTerminal, score = terminal(state)
        if isTerminal:
            return score

        actions = action(state)

        if isMaximize:
            maxEval = float('-inf')
            for move in actions:
                eval = self.minimax(result(state, move), False)
                maxEval = max(maxEval, eval)
            return maxEval
        else: # MinAgent
            minEval = float('inf')
            for move in actions:
                eval = self.minimax(result(state, move), True)
                minEval = min(minEval, eval)
            return minEval

    def getMove(self, state: list) -> tuple:
        actions = action(state)
        bestMove = None
        if self.max == 'X':
            bestScore = float('-inf')
            for move in actions:
                newState = result(state, move)
                score = self.minimax(newState, False)

                if score > bestScore:
                    bestScore = score
                    bestMove = move
        else:
           bestScore = float('inf')
           for move in actions:
               newState = result(state, move)
               score = self.minimax(newState, True)

               if score < bestScore:
                   bestScore = score
                   bestMove = move

        return bestMove




if __name__ == '__main__':
    mm = MinimaxAgent('X')
    print(mm.getMove(almostTerminalXState()))
