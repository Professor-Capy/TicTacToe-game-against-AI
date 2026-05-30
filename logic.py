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
    
