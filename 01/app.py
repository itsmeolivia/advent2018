filename = "frequency.txt"

def findRepeat(filename):
    a_file = open(filename, "r")
    start = 0
    seen = set()
    while True:
        for line in a_file:
            start += int(line)
            if start in seen:
                print start
                return
            else:
                seen.add(start)
        a_file.close()
        a_file = open(filename, "r")

findRepeat(filename)
