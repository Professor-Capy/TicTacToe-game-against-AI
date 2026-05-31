state is a 2d list, basically just a grid, empty spaces are js hashtags
an example of an empty state looks like this
[['#', '#', '#'],
 ['#', '#', '#'],
 ['#', '#', '#']]

X ALWAYS plays first, some code is based on that assumption

i guess dataStructs also has a Queue, but its not rly needed here

player function accepts a singular param state, which is used for
determining the player

result function accepts 2 params, currentState, and move
it is used for finding the result of an action

action function accepts 1 param, state
is used for finding all possible moves and
returns an answer in the form of a tuple

terminal function accepts 1 param, state, and returns a tuple, in format of:
(isTerminalState: bool, points: int)
in actual code you'll see the points as utility, bcuz utility returns an int
this func is used for determining if a state is a terminal state, meaning if the game is over

utility function accepts 1 optional param, winner, with a default value of None
it is used for finding the point for each winner of the game
