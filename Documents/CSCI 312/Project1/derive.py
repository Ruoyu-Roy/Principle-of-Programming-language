import sys
import string
import os

if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Format: python derive.py [-l length] grammarfile")
    sys.exit()

if len(sys.argv) == 2:
    stringLength = 3
    if os.path.isfile(sys.argv[1]):
        grammarfile = sys.argv[1]
    else:
        print("No such test file exists...")
elif len(sys.argv) == 3:
    if sys.argv[1] == "-l":
        stringLength = 3
    else:
        stringLength = int(sys.argv[1].strip("-l"))
    if os.path.isfile(sys.argv[2]):
        grammarfile = sys.argv[2]
    else:
        print("No such test file exists...")

# Production Dictionary
proDict = {}
# List of candidate terminal strings
worklist = []
# Whether it is a start symbol
start = True

# Store all the productions
for line in open(grammarfile, "r"):
    emptylist = []
    lhs = line.split()[0]
    rhs = line.split()[2:]
    emptylist.append(lhs)
    if start:
        worklist.append(emptylist)
        start = False
    if not proDict.has_key(lhs):
        proDict[lhs] = []
    proDict[lhs].append(rhs)

def checkNonTerminal(sententce):
    for symbol in sentence:
        if (proDict.has_key(symbol)):
            return 1
    return 0

def findLeftMostNT(sententce):
    count = 0
    for symbol in sentence:
        if (proDict.has_key(symbol)):
            return count
        count += 1
    return -1

while len(worklist) > 0:
    sentence = worklist.pop(0)
    if len(sentence) > stringLength:
        continue
    if checkNonTerminal(sentence) == 0:
        i = 1
        for symbol in sentence:
            i += 1
            print symbol,
        print "\n",
        continue
    if findLeftMostNT(sentence) != -1:
        index = findLeftMostNT(sentence)
        for rhs in proDict[sentence[index]]:
            tmp = []
            tmp.extend(sentence)
            tmp.pop(index)
            count = index
            for symbol in rhs:
                tmp.insert(count, symbol)
                count += 1
            worklist.append(tmp)
