import unittest
import sys
sys.path.append('2023/')

from day01_Trebuchet import part1, part2

class Test_2023_01(unittest.TestCase):
    data_1 = '''
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        '''
    data_2 = '''
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        '''
        
    def test_part1(self):
        values = [i for i in (line.strip() for line in self.data_1.splitlines()) if i]
        r = 142
        self.assertEqual(part1(values), r)

    def test_part2(self):
        values = [i for i in (line.strip() for line in self.data_2.splitlines()) if i]
        r = 281
        self.assertEqual(part2(values), r)

if __name__ == '__main__':
    unittest.main()