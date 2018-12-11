from collections import Counter

def threeAndTwoCount(word):
    c_word = Counter(word)
    three = 0
    two = 0
    for elem, count in c_word.items():
        if count == 3:
            three = 1
        if count == 2:
            two = 1
    return two, three

def checksum():
    filename = "input.txt"
    file = open(filename, "r")


    two_count = 0
    three_count = 0
    for line in file:
        print line
        two, three = threeAndTwoCount(line)
        two_count += two
        three_count += three
    return two_count * three_count

def findTheBoxes():
    filename = "input.txt"
    file = open(filename, "r")

    queue = []
    for line in file:
        queue.append(line[1:])
    queue.sort()
    prev = queue[0]
    for pos in xrange(1, len(queue)):
        for letter in "abcdefghijklmnopqrstuvwxyz":
            for i in xrange(len(prev) - 1):
                new_word = prev[:i] + letter + prev[i + 1:]
                if new_word == queue[pos]:
                    return new_word, queue[pos]

        prev = queue[pos]

print findTheBoxes()
