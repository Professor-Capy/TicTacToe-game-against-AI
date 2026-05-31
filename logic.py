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
    # check for a winner first
    for player in ['X', 'O']:
        # Check Rows
        for r in range(3):
            if state[r][0] == player and state[r][1] == player and state[r][2] == player:
                return (True, utility(player))

        # Check Columns
        for c in range(3):
            if state[0][c] == player and state[1][c] == player and state[2][c] == player:
                return (True, utility(player))

        # Check Main Diagonal (Top-Left to Bottom-Right)
        if state[0][0] == player and state[1][1] == player and state[2][2] == player:
            return (True, utility(player))

        # Check Anti-Diagonal (Top-Right to Bottom-Left)
        if state[0][2] == player and state[1][1] == player and state[2][0] == player:
            return (True, utility(player))

    # 2. Check for a Draw/Tie (No empty spaces left, and nobody won)
    emptySpaces = action(state)
    if not emptySpaces:
        return (True, utility())  # Assuming utility() with no args implies a tie (e.g., 0)

    # 3. Game is still ongoing
    return (False, None)


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

