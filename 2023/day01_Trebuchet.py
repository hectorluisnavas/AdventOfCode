# Day 1: Trebuchet?!
# https://adventofcode.com/2023/day/1

import re
from utils.timeit import timeit

# Solution Part 1
@timeit
def part1(list: list) -> int:
    total = 0
    for line in list:
        i = [int(i) for i in line if i.isdigit()]
        
        if len(i) >= 2:
            total += int( str(i[0]) + str(i[-1]))
        else:
            total += int( str(i[0]) + str(i[0]))
    
    return total

# Solution Part 2
@timeit
def part2(list: list) -> int:
    data = []
    PATTERN = r'one|two|three|four|five|six|seven|eight|nine|\d+'
    d = {
      'one' : '1',
      'two' : '2',
      'three' : '3',
      'four' : '4',
      'five' : '5',
      'six' : '6',
      'seven' : '7',
      'eight' : '8',
      'nine' : '9'
    }

    for line in list:
        w = []
        match = re.search(PATTERN, line)

        while match:
            w.append(match.group())
            next = match.start() + 1
            line = line[next:]
            match = re.search(PATTERN, line)
        
        w = [ d[i] if i in d else i for i in w ]
        r = ''.join( i for i in w)
        data.append(r)

    return part1(data)

if __name__ == '__main__':
    with open('2023/data/data-d01.txt') as file:
        data = [line.strip() for line in file]
    
    print('Part 1 => ', part1(data))
    print('Part 1 => ', part2(data))