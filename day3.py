import re
import time
start_time = time.time()

file = open('day3.txt', 'r')
text = file.read()
file.close()

def getMultiplications(text):
    multiplicationPattern = r'mul\(\d{1,3},\d{1,3}\)'
    return re.findall(multiplicationPattern, text)

def getMultiplicationResult(multiplication):
    factor1, factor2 = multiplication[4:-1].split(',')
    return int(factor1) * int(factor2)

def getMultiplicationsSum():
    total = 0
    for multiplication in getMultiplications(text):
        total += getMultiplicationResult(multiplication)
    return total

# Array of text chunks starting with do() and ending with don't()
def getEnabledChunks():
    enabledChunksPattern = r'do\(\)[\s\S]*?don\'t\(\)'
    defaultChunkPattern = r'^[\s\S]*?do\(\)' # chunk before first do()
    
    defaultChunk = re.search(defaultChunkPattern, text).group(0)
    if defaultChunk != None:
        return [defaultChunk] + re.findall(enabledChunksPattern, text) #TODO get last chunk after potential do()
    return re.findall(enabledChunksPattern, text)

def getEnabledMultiplicationSum():
    total = 0
    print(len(getEnabledChunks()))
    for chunk in getEnabledChunks():
        for multiplication in getMultiplications(chunk):
            total += getMultiplicationResult(multiplication)
    return total

print(getMultiplicationsSum())
print("--- %s seconds ---" % (time.time() - start_time))
# print(getEnabledMultiplicationSum())