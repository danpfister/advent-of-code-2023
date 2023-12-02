import numpy as np
import re

def part1(inputdata):
    count_possible = 0
    for line in inputdata:
        game_nr = re.search(r'Game (\d+).+', line)[1]
        count = {'red': 0, 'green': 0, 'blue': 0}
        sets = line.split(';')
        for set in sets:
            matches = re.findall(r'\s(\d+)\s(\w+).?', set)
            for match in matches:
                number, color = match
                count[color] = int(number) if int(number) > count[color] else count[color]
        if count['red'] <= 12 and count['green'] <= 13 and count['blue'] <= 14:
            count_possible += int(game_nr)
    print(f"the sum of the indices of the possible games is {count_possible}")
        
                
def part2(inputdata):
    sum_of_powers = 0
    for line in inputdata:
        sets = line.split(';')
        count = {'red': 0, 'green': 0, 'blue': 0}
        for set in sets:
            matches = re.findall(r'\s(\d+)\s(\w+).?', set)
            for match in matches:
                number, color = match
                count[color] = int(number) if int(number) > count[color] else count[color]
        sum_of_powers += count['red'] * count['green'] * count['blue']
    print(f"the sum of the powers of the sets is {sum_of_powers}")
        
    
if __name__ == '__main__':
    inputfile = open(r'C:\Users\Daniel\Github\advent-of-code-2023\day02\input.txt', 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    part1(inputdata)
    part2(inputdata)