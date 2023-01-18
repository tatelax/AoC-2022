input = open("day1.txt").read()

calories = input.split("\n\n")

highestSum = 0
secondHighestSum = 0
thirdHighestSum = 0

for elf in calories:
    total = elf.split('\n');

    sum = 0

    for item in total:
        if item != '':
            sum += int(item)

    if sum > highestSum:
        thirdHighestSum = secondHighestSum
        secondHighestSum = highestSum
        highestSum = sum
    elif sum > secondHighestSum:
        thirdHighestSum = secondHighestSum
        secondHighestSum = sum
    elif sum > thirdHighestSum:
        thirdHighestSum = sum


print(highestSum + secondHighestSum + thirdHighestSum)