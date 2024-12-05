file = open('day4.txt', 'r')
lines = file.readlines()
file.close()

def isWord(string, word):
    return string == word or string == word[::-1]

def getHorizontalWordAmount(word):
    total = 0
    for j in range(len(lines)):
        for i in range(len(lines[0]) - len(word)):   
            total += isWord(lines[j][i:i + len(word)], word)
    return total

def getVerticalWordAmount(word):
    total = 0
    for i in range(len(lines[0])):
        for j in range(len(lines) - len(word) + 1):
            string = ''.join([line[i] for line in lines[j:j + len(word)]])
            total += isWord(string, word)
    return total

""" diagonal right : / """ 
def getDiagonalRightWordAmount(word):
    total = 0
    for j in range(len(lines) - len(word) + 1):
        for i in range(len(word) - 1, len(lines[0])):
            string = ''.join([lines[j + z][i - z] for z in range(len(word))])
            total += isWord(string, word)
            print(string)
    return total

""" diagonal left : \ """
def getDiagonalLeftWordAmount(word):
    total = 0
    for j in range(len(lines) - len(word) + 1):
        for i in range(len(lines[0]) - len(word)):
            string = ''.join([lines[j + z][i + z] for z in range(len(word))])
            total += isWord(string, word)
    return total

def getWordAmount(word):
    return getHorizontalWordAmount(word) + getVerticalWordAmount(word) + getDiagonalRightWordAmount(word) + getDiagonalLeftWordAmount(word)

def getXmaxAmount():
    total = 0
    for j in range(1, len(lines) - 1):
        for i in range(1, len(lines[0]) - 1):
            if lines[j][i] == 'A':
                diagonal_right = [lines[j - 1][i + 1], lines[j + 1][i - 1]]
                diagonal_left = [lines[j - 1][i - 1], lines[j + 1][i + 1]]
                total += isXmas(diagonal_right, diagonal_left)
    return total

def isXmas(diagonal_right, diagonal_left):
    diagonal_sum = ord('M') + ord('S')
    diagonal_right_sum = sum([ord(diagonal_letter) for diagonal_letter in diagonal_right])
    diagonal_left_sum = sum([ord(diagonal_letter) for diagonal_letter in diagonal_left])

    return diagonal_right_sum == diagonal_sum and diagonal_left_sum == diagonal_sum

# print(getWordAmount('XMAS'))
print(getXmaxAmount())