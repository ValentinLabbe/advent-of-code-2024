file = open('day1.txt', 'r')
lines = file.readlines()
file.close()

data = [line.split() for line in lines]
left_list = [int(numbers[0]) for numbers in data]
right_list = [int(numbers[1]) for numbers in data]

def getCumulatedDistance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total = 0
    if (len(left_list) != len(right_list)):
        return False
    for i in range(len(left_list)):
        total += abs(left_list[i] - right_list[i])
    return total

def getSimilarityScore(left_list, right_list):
    total = 0
    numbers_count = {}
    for number in right_list:
        numbers_count[number] = numbers_count.get(number, 0) + 1
    for number in left_list:
        if number in numbers_count:
            total += number * numbers_count.get(number, 0)
    return total


print(getCumulatedDistance(left_list, right_list))
print(getSimilarityScore(left_list, right_list))