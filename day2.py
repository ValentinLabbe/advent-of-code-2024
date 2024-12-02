file = open('day2.txt', 'r')
lines = file.readlines()
file.close()

records = [[int(number) for number in line.split()] for line in lines]

def isRecordSafe(record):
    return (isRecordIncreasing(record) or isRecordDecreasing(record)) and isRecordAdjacentNumbersDistanceBetweenOneAndThree(record)

def isRecordIncreasing(record):
    return sorted(record) == record

def isRecordDecreasing(record):
    return sorted(record, reverse=True) == record

def isRecordAdjacentNumbersDistanceBetweenOneAndThree(record):
    for i in range(len(record) - 1):
        distance = abs(record[i] - record[i + 1])
        if (distance < 1 or distance > 3):
            return False
    return True

def getSafeRecordsAmount():
    total = 0
    for record in records:
        if isRecordSafe(record):
            total += 1
    return total

def isRecordSafeWithProblemDampener(record):
    if (isRecordSafe(record)):
        return True
    for i in range(1, len(record) + 1):
        if (isRecordSafe(record[0:i-1] + record[i:])):
            return True
    return False

def getSafeRecordsAmountWithProblemDampener():
    total = 0
    for record in records:
        if isRecordSafeWithProblemDampener(record):
            total += 1
    return total

    
print(getSafeRecordsAmount())
print(getSafeRecordsAmountWithProblemDampener())