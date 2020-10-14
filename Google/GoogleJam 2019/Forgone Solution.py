import random
def generateSequence(number) :
    sequence = [loopVar for loopVar in range(number + 1)]
    if 4 in sequence :
        sequence.remove(4)
    return sequence
testCase=int(input())
resultSet = []
while testCase > 0 :
    testCase -= 1
    numberSet1 = []
    numberSet2 = []
    number = input()
    digitList = list(map(int,list(str(number))))
    for loopVar in digitList :
        while True :
            randomNumber = random.choice(generateSequence(loopVar))
            if abs(randomNumber - loopVar) != 4 :
                break    
        numberSet1.append(randomNumber)
        numberSet2.append(abs(randomNumber - loopVar))
    answerSet = []
    answerSet.append(int("".join(list(map(str,numberSet1)))))
    answerSet.append(int("".join(list(map(str,numberSet2)))))
    resultSet.append(answerSet)
for loopVar in range(len(resultSet)) :
    print ("Case #{0}: {1} {2}".format(loopVar + 1,resultSet[loopVar][0],resultSet[loopVar][1]))