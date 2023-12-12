import numpy as np
from itertools import product

symbols = ['#', '.']

def check_validity(combination, group):
    hashes = [g for g in combination.split('.') if g]
    if len(hashes) != len(group): return False
    for hash, g in zip(hashes, group):
        if len(hash) != g: return False
    return True

def parse_input(inputdata):
    data = [line.split() for line in inputdata]
    springs = [line[0] for line in data]
    groups = [[int(num) for num in line[1].split(',')] for line in data]
    return springs, groups

def part1and2(inputdata):
    springs, groups = parse_input(inputdata)
    valid_combinations = 0
    for spring, group in zip(springs, groups):
        nr_of_qmarks = spring.count('?')
        combinations = product(symbols, repeat=nr_of_qmarks)
        for combination in combinations:
            combination_str = list(''.join(combination))
            replaced = ''.join([char if char != '?' else combination_str.pop(0) for char in spring])
            if check_validity(replaced, group): valid_combinations += 1
    print(f"PART 1: the sum of the possible arrangements of springs is: {valid_combinations}")
        

def part2(inputdata): pass

if __name__ == '__main__':
    inputfile = open(r'C:\Users\danpf\Github\advent-of-code-2023\day12\test.txt', 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    part1and2(inputdata)