import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random


myID, game_map = hlt.get_init()
hlt.send_init("rhyuenBot")

def findNearestOppDirection(square):
    direction = NORTH
    maxDistance = min(game_map.width, game_map.height)/2

    #start loop
    distance = 0
    current = square
    site = game_map.get



    return direction


def assign_move(square):
    border = False
    ###On Border, Can I Win?
    for direction, neighbor in enumerate(game_map.neighbors(square)):
        if neighbor.owner != myID:
            border = True
            if neighbor.strength < square.strength:
                return Move(square, direction)

    ###Not enough power, build it.
    if square.strength < 5 * square.production:
        return Move(square, STILL)

    ###Not on border, advance territory.
    if border == False:
        return Move(square, random.choice((NORTH, WEST)))

    #On Border, but can't win. Hold position.
    return Move(square, STILL)

while True:
    game_map.get_frame()
    moves = [assign_move(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
