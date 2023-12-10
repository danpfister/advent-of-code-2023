import numpy as np
import re

# describe what symbol needs to be below/above/left/right for there to be a connection
movements = {
    'down': [1, 0],
    'up': [-1, 0],
    'left': [0, -1],
    'right': [0, 1]}
connections = {
    '|': ['up', 'down'],
    '-': ['left', 'right'],
    'L': ['up', 'right'],
    'J': ['up', 'left'],
    '7': ['down', 'left'],
    'F': ['down', 'right']
}

def find_connection(inputdata, current_position, previous_position):
    current_position = np.asarray(current_position)
    for movement, direction in movements.items():
        if np.array_equal(current_position+direction, previous_position): continue # skip the position we just came from
        next_position = np.array(current_position)+direction
        try: # in case it tries to read values outside of the array
            current_symbol = inputdata[*current_position]
        except:
            print(f"out of bounds")
            continue
        if movement in connections[current_symbol]:
            return next_position
        

def part1(inputdata):
    start = np.argwhere(inputdata == 'S')[0]
    current_pos = [114, 40] # TODO hardcoded for now
    previous_pos = start
    steps = 1
    
    while not np.array_equal(current_pos, start): # loop until we're back at the start
        next_pos = find_connection(inputdata, current_pos, previous_pos)
        previous_pos = current_pos
        current_pos = next_pos
        steps += 1
    
    print(f"PART 1: the number of steps to the farthest point on the loop is {int(steps/2)}")
    
    

if __name__ == '__main__':
    inputfile = open(r'C:\Users\Daniel\Github\advent-of-code-2023\day10\input.txt', 'r')
    inputdata = np.asarray([[char for char in line.strip()] for line in inputfile])
    part1(inputdata)