from typing import Optional
# used for determining the player
def player(state: list) -> str:
    x: int = 0
    o: int = 0
    for row in state: # for each row of the board in the current state
        for box in row: # and for each box in that row
            # it isnt that hard cmon now
            match box:
                case 'X':
                    x += 1
                case 'O':
                    o += 1

    # X always plays first, so if x isnt greater than o,
    # it is equal to o, removing the need for an else statement
    if x > o:
        return 'O'
    return 'X'

# Used to find the result of an action (move)
def result(currentState: list, move: tuple) -> list:
     row, col = move # unpacks move
     # the slicing is important, cuz it tells py to make a new
     # instance in memory for the copy, cuz python lists are pointers
     # to the actual list, hidden somewhere else in memory
     copyState = [row[:] for row in currentState]

     currentPlayer = player(currentState)
     copyState[row][col] = currentPlayer
     return copyState

# Used for finding all available moves
def action(state: list) -> tuple: # it returns a tuple of tuples
    possibleActions = []
    r = 0
    for row in state:
        c = 0
        for box in row:
            if box == '#':
                possibleActions.append((r, c))

        c += 1
        r += 1

    return tuple(possibleActions)

# Will be used for determining if a state is a 'terminal' state
# A state is terminal if:
# A. One agent won the game (aka the other agent lost)
# B. No available moves are left (draw/tie)
# will return a tuple in format of:
# (isTerminalState: bool, winner: str | None)
def terminal(state: list) -> tuple:
    # Check if draw/tie

    emptySpaces: tuple = action(state)
    # empty data structs in py are falsy
    # and if action finds no empty spaces, it will return an empty tuple
    # so basically, this checks if any moves are still available
    # and if no moves are available, that means its a draw
    if not emptySpaces:
        return (True, utility())

    xSpace: dict = {0: [],
                    1: [],
                    2: []}
    oSpace: dict = {0: [],
                    1: [],
                    2: []}
    r: int = 0
    copyState = [row[:] for row in state]
    for row in copyState:
        for i in range(len(row) - 1, -1, -1): # loops through it backwards
            box = row[i]
            match box:
                case 'X':
                    xSpace[r].append(i)
                    row.pop(i)
                case 'O':
                    oSpace[r].append(i)
                    row.pop(i)
        r += 1

    # checking for horizontal win
    for i in range(0, 3):
        if len(xSpace[i]) == 3:
            return (True, utility('X'))
        elif len(oSpace[i]) == 3:
            return (True, utility('O'))

    # checking for vertical win
    for i in range(0, 3):
        if sum(xSpace[i]) == 3:
            return (True, utility('X'))
        elif sum(oSpace[i]) == 3:
            return (True, utility('O'))

    # check for diagonal win
    


def utility(winner: str | None = None) -> int:
    pass

# Use this for testing
if  __name__ == '__main__':
    emptyState = [['#', '#', '#'],
                  ['#', '#', '#'],
                  ['#', '#', '#']]
    terminalOState = [['O', 'X', '#'],
                      ['O', 'X', 'X'],
                      ['O', 'O', 'X']]
    terminalXState = [['X', 'O', 'X'],
                      ['#', 'X', 'O'],
                      ['O', '#', 'X']]
    terminalDrawState = [['O', 'X', 'O'],
                         ['O', 'X', 'X'],
                         ['X', 'O', 'X']]
    print(terminal(emptyState))

