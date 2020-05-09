import random

#################### CONSTANT ####################

WUMPUS_WORLD_DIMENSION = 3

WUMPUS = 'W'
PIT = 'p'
AGENT = 'A'
GOLD = 'G'

# SENSORS

STENCH = 's'
BREEZE = 'b'
GLITTER = 'g'
BUMP = 'b'
SCREAM = 'sc'
NONE = 'n'

# SYMBOL

OK = 'ok'
VISITED = 'v'

#################### WUMPUS WORLD ####################

world = [['', '', '', ''],
         ['', '', '', ''],
         ['', '', '', ''],
         ['', '', '', '']]


#################### METHODS ####################

def get_random_position():
    x = random.randint(0, WUMPUS_WORLD_DIMENSION)
    y = random.randint(0, WUMPUS_WORLD_DIMENSION)

    return x, y


def is_wall(x, y):
    if x < 0 or x > WUMPUS_WORLD_DIMENSION or y < 0 or y > WUMPUS_WORLD_DIMENSION:
        return True
    else:
        return False


def add(x, y, value):
    if value != "" and is_wall(x, y) == False:
        if world[x][y] == "":
            world[x][y] = value
        else:
            world[x][y] += "," + value


def find(x, y, value):
    currentValue = world[x][y]
    values = currentValue.split(',')
    for i in range(len(values)):
        if values[i] == value:
            return True
    return False


def set_wumpus():
    x, y = get_random_position()
    if x == 0 and y == 0:
        set_wumpus()
    else:
        if find(x, y, WUMPUS):
            set_wumpus()
        else:
            # set wumpus
            add(x, y, WUMPUS)
            # set sensors
            add(x+1, y, STENCH)
            add(x-1, y, STENCH)
            add(x, y+1, STENCH)
            add(x, y-1, STENCH)


def set_pit():
    x, y = get_random_position()
    if x == 0 and y == 0:
        set_pit()
    else:
        if find(x, y, PIT):
            set_pit()
        else:
            # set pit
            add(x, y, PIT)
            # set sensors
            add(x+1, y, BREEZE)
            add(x-1, y, BREEZE)
            add(x, y+1, BREEZE)
            add(x, y-1, BREEZE)


def set_gold():
    x, y = get_random_position()
    if x == 0 and y == 0:
        set_gold()
    else:
        if find(x, y, GOLD):
            set_gold()
        else:
            # set pit
            add(x, y, GOLD)
            # set sensors
            add(x, y, GLITTER)

#################### INITIALIZE WUMPUS WORLD ####################


set_wumpus()
set_pit()
set_pit()
set_pit()
set_gold()

print(world[0])
print(world[1])
print(world[2])
print(world[3])

#################### EXPLORING THE WUMPUS WORLD ####################

