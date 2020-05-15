import random

#################### CONSTANT ####################

WUMPUS_WORLD_DIMENSION = 3
SEPARATOR = ','

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

world = [[AGENT, '', '', ''],
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
        if is_empty(x, y):
            world[x][y] = value
        else:
            if find(x, y, value) == False:
                world[x][y] += SEPARATOR + value


def remove(x, y, value):
    if is_wall(x, y) == False:
        values = world[x][y]
        world[x][y] = values.replace(SEPARATOR + value, '').replace(value, '')


def find(x, y, value):
    currentValue = world[x][y]
    values = currentValue.split(SEPARATOR)
    for i in range(len(values)):
        if values[i] == value:
            return True
    return False


def is_empty(x, y):
    if is_wall(x, y) == False:
        if world[x][y] == "":
            return True
    else:
        False


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


def build_world():
    set_wumpus()
    set_pit()
    set_pit()
    set_pit()
    set_gold()

    print_world()


def print_world():
    print(world[0])
    print(world[1])
    print(world[2])
    print(world[3])
    print('')

#################### AGENT METHODS ####################


"""
POSITION MAP

[[0,0],[0,1],[0,2],[0,3],
 [1,0],[1,1],[1,2],[1,3],
 [2,0],[2,1],[2,2],[2,3],
 [3,0],[3,1],[3,2],[3,3]]

"""


def get_information(x, y):

    if is_wall(x, y):
        return {
            "bump": True
        }
    else:
        return {
            "bump": False,
            "stench": find(x, y, STENCH),
            "breeze": find(x, y, BREEZE),
            "glitter": find(x, y, GLITTER),
            "visited": find(x, y, VISITED),
            "ok": find(x, y, OK)
        }


"""
   │ F │
───┼───┼───
 L │ A │ R
───┼───┼───
   │ B │

A: Agent position   (x,y)
L: Left             (x-1,y)
R: Right            (x-1,y)
F: Forward          (x,y+1)
B: Backward         (x,y-1)
"""


def next(x, y):
    # check current position
    if is_empty(x, y):
        add(x, y, OK)

    current = get_information(x, y)
    left = get_information(x - 1, y)
    right = get_information(x + 1, y)
    forward = get_information(x, y+1)
    backward = get_information(x, y-1)
    # use all information to make a move.
    if left.bump == False and forward.bump == False and right.bump == False and forward.bump == False:
        print('All Information')

    if left.bump == True:
        if forward.bump == True:
            # Agent is in a corner 
            if backward.bump == False and right.bump == False:
"""
   │   │
───┼───┼───
   │ b │ b
───┼───┼───
   │ b │ 
"""
                # use backward and right to take a desition.
                if current.breeze == True and 

        # use left, forward and current information to make a move.
        


def check_stauts(x, y):
    agent_die = False
    found_gold = find(x, y, GOLD)

    if find(x, y, WUMPUS) or find(x, y, PIT):
        agent_die = True

    return found_gold, agent_die


def exploring_world():
    current_x = 0
    current_y = 0

    limit = 0

    while found_gold == False and agent_die == False and limit < 100:

        current_x, current_y = next(current_x, current_y)

        found_gold, agent_die = check_stauts(current_x, current_y)
        # add(new_x, new_y, AGENT)
        # remove(current_x, current_y, AGENT)
        # add(current_x, current_y, VISITED)
        print_world()
        limit += 1

    if found_gold:
        print("Gold is found")

    if agent_die:
        print("agent is died")

    if limit > 98:
        print("Infinite loop")

#################### INITIALIZE WUMPUS WORLD ####################


build_world()

#################### EXPLORING THE WUMPUS WORLD ####################

exploring_world()
