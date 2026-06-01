def emptyState():
    return [['#', '#', '#'],
            ['#', '#', '#'],
            ['#', '#', '#']]

def terminalOState():
    return [['O', 'X', '#'],
            ['O', 'X', 'X'],
            ['O', 'O', 'X']]

def terminalXState():
    return [['X', 'O', 'X'],
            ['#', 'X', 'O'],
            ['O', '#', 'X']]

def terminalDrawState():
    return [['O', 'X', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'X']]
