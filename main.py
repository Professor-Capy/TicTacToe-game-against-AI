from display import display
from agent import MinimaxAgent
from logic import terminal, result
from testStates import emptyState

def main():
    state = emptyState()
    oPlayer = MinimaxAgent('O')
    xPlayer = MinimaxAgent('X')

    currentPlayer = 'X'
    while True:
        display(state)
        isTerminal, winner = terminal(state)
        if isTerminal:
            break

        if currentPlayer == 'X':
            xMove = xPlayer.getMove(state)
            if not xMove:
                break
            state = result(state, xMove) # the getMove returns a coord similar to an action
            currentPlayer = 'O'
        elif currentPlayer == 'O':
            oMove = oPlayer.getMove(state)
            if not oMove:
                break
            state = result(state, oMove)
            currentPlayer = 'X'

    print()
    match winner:
        case 0:
            print('Its a draw!')
        case 1:
            print('X wins')
        case -1:
            print('O wins')

if __name__ == '__main__':
    main()
