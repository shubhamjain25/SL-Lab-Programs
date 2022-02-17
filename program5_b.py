# To run just do: python program5_b.py temp.txt

import os
import sys
from functools import reduce

dict = {}
wordLen = []

if len(sys.argv) != 2:
    print("Invalid Arguments")
    sys.exit()

if not(os.path.exists(sys.argv[0])):
    print("File does not exist")
    sys.exit()

if sys.argv[1].split(".")[-1] != "txt":
    print("Only TXT files allowed")
    sys.exit()

with open(sys.argv[1]) as file:
    for line in file:
        for word in line.split():
            dict[word] = dict.get(word, 0) + 1

sortedDict = sorted(dict.items(), key=lambda dictItem: dictItem[1], reverse=True)

for i in range(10):
    try:
        wordTuple = sortedDict[i]
        print("Word: ", wordTuple[0], " Frequency: ", wordTuple[1], " Length: ", len(wordTuple[0]))
        wordLen.append(len(wordTuple[0]))
    except IndexError:
        print("File contains less than 10 words")

sum = reduce(lambda x, y: x+y, wordLen)
print("Average word-lengths: ", sum/len(wordLen))

squares = [x**2 for x in wordLen if x % 2 != 0]
print ("Squares of odd word lengths: ")
print (squares)
