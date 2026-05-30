# used for determining the player
def player(state: list):
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

def result(currentState, actionState):
    pass
