input = open("day3.txt").read()

rucksacks = input.split('\n');
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
totalSum = 0

for rucksack in rucksacks:
    head = 0;
    tail = len(rucksack) - 1;

    itemsLhs = set()
    itemsRhs = set()

    while(head < len(rucksack) / 2):
        itemsLhs.add(rucksack[head])
        itemsRhs.add(rucksack[tail])

        head += 1;
        tail -= 1;

    for item in itemsLhs:
        if item in itemsRhs:
            totalSum += int(alphabet.find(item) + 1)

print(totalSum)


#############   PART 2   #################


input = open("day3.txt").read()

rucksacks = input.split('\n');
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
totalSum = 0

rucksackA = set()
rucksackB = set()
rucksackC = set()

def FindCommonLetter():
    total = 0;

    for item in rucksackA:
        if item in rucksackB and item in rucksackC:
            total += int(alphabet.find(item) + 1)

    return total;

i = 0
for rucksack in rucksacks:
    if i == 0:
        for item in rucksack:
            rucksackA.update(item)
    elif i == 1:
        for item in rucksack:
            rucksackB.update(item)
    elif i == 2:
        for item in rucksack:
            rucksackC.update(item)

    i += 1

    if i == 3:
        totalSum += FindCommonLetter()
        rucksackA.clear()
        rucksackB.clear()
        rucksackC.clear()
        i = 0

print(totalSum)