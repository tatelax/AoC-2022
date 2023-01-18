input = open("day4.txt").read()

pairs = input.split("\n");

total = 0

for pair in pairs:
    sections = pair.split(",");
    sectionRangeA = sections[0]
    sectionRangeB = sections[1]

    sectionRangeASplit = sectionRangeA.split("-")
    sectionRangeBSplit = sectionRangeB.split("-")

    section0 = int(sectionRangeASplit[0])
    section1 = int(sectionRangeASplit[1])
    section2 = int(sectionRangeBSplit[0])
    section3 = int(sectionRangeBSplit[1])

    if (section0 <= section2 and section1 >= section3) or (section2 <= section0 and section3 >= section1):
        print(pair)
        total += 1

print(f'Total: {total}')
