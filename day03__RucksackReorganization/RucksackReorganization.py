"""Created on Dec 08 23:42:24 2022."""

from _backend__part1 import rucksack_reorganization
from _backend__part2 import rucksack_batch_reorganization

temp1 = rucksack_reorganization('./RucksackReorganization__submit.txt')
temp2 = rucksack_batch_reorganization('./RucksackReorganization__submit.txt')

print(temp1)
print(temp2)
