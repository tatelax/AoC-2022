input = open("day2.txt").read()

turns = input.split("\n");

myScore = 0

def calcScore(opponentMove, myMove):
    if opponentMove == "A" and myMove == "X":
        return 4
    elif opponentMove == "A" and myMove == "Y":
        return 8
    elif opponentMove == "A" and myMove == "Z":
        return 3
    elif opponentMove == "B" and myMove == "X":
        return 1
    elif opponentMove == "B" and myMove == "Y":
        return 5
    elif opponentMove == "B" and myMove == "Z":
        return 9
    elif opponentMove == "C" and myMove == "X":
        return 7
    elif opponentMove == "C" and myMove == "Y":
        return 2
    elif opponentMove == "C" and myMove == "Z":
        return 6

    return 0

def determineMove(input, output):
    if input == "A" and output == "X":
        return "Z"
    elif input == "A" and output == "Y":
        return "X"
    elif input == "A" and output == "Z":
        return "Y"
    elif input == "B" and output == "X":
        return "X"
    elif input == "B" and output == "Y":
        return "Y"
    elif input == "B" and output == "Z":
        return "Z"
    elif input == "C" and output == "X":
        return "Y"
    elif input == "C" and output == "Y":
        return "Z"
    elif input == "C" and output == "Z":
        return "X"

for turn in turns:
    moves = turn.split(" ");
    myScore += calcScore(moves[0], determineMove(moves[0], moves[1]));

print(myScore);