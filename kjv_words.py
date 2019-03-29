fin = open("kjv.txt")

def wordCount(a, b):
    count = 0
    for line in fin:
        line = line.lower()
        if a in line and b in line:
            count += 1
    return count

print(wordCount("good", "evil"))

fin.close()
