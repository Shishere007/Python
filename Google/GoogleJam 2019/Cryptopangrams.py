import math
import string
def computeGCD(number1,number2) :
    while number2 :
        number1,number2 = number2, number1 % number2
    return number1
def readProductList(count) :
    productList = list(map(int,input().split()))
    return productList
def listFactor(productList) :
    factorsList= []
    commonDiv = computeGCD(productList[0],productList[1])
    factorsList.append([int(productList[0] / commonDiv),commonDiv])
    for loopVar in range(len(productList) - 1) :
        commonDiv = computeGCD(productList[loopVar],productList[loopVar + 1])
        factorsList.append([commonDiv,productList[loopVar] // commonDiv])
    commonDiv = computeGCD(productList[-1],productList[-2])
    factorsList.append([int(productList[-1] / commonDiv),commonDiv])
    return factorsList
def singleList(factorList) :
    tempList = []
    for loopVar in factorList :
        for loopVar2 in loopVar :
            tempList.append(loopVar2)
    tempList.sort()
    for loopVar in tempList :
        while tempList.count(loopVar) != 1 :
            tempList.remove(loopVar)
    return tempList
def assignAlpha(factorList) :
    numberList = singleList(factorList)
    alphaList = list(string.ascii_uppercase)
    crypticCode = {}
    for loopVar in range(len(alphaList)) :
        crypticCode[numberList[loopVar]] = alphaList[loopVar]
    return crypticCode
def decypher(cryptMessage,crypticCode) :
    message = []
    for loopVar in cryptMessage :
        message.append(crypticCode[loopVar])
    textMessage = "".join(message)
    return textMessage
def genCrypticMessage(numberFactorList) :
    tempList = []
    tempList.append(numberFactorList[0][0])
    for loopVar in numberFactorList :
        tempList.append(loopVar[-1])
    return tempList
def orderFactor(tempList) :
    ansList = []
    if tempList[0][-1] not in tempList[1] :
        ansList[0].append(tempList[0][::-1])
    else :
        ansList.append(tempList[0])
    for loopVar in range(len(tempList) - 1) :
        if ansList[loopVar][-1] == tempList[loopVar + 1][0] :
            ansList.append(tempList[loopVar + 1])
        else :
            ansList.append(tempList[loopVar + 1][::-1])
    return ansList
testCase = int(input())
resultSet = []
for loopVar in range(testCase) :
    read = list(map(int,input().split()))
    number = read[0]
    productCount = read[1]
    productList = readProductList(productCount)
    numberFactorList = listFactor(productList)
    numberFactorList = orderFactor(numberFactorList)
    crypticMessage = genCrypticMessage(numberFactorList)
    crypticCode = assignAlpha(numberFactorList)
    textMessage = decypher(crypticMessage,crypticCode)
    resultSet.append(textMessage)
for loopVar in range(len(resultSet)) :
    print ("Case #{0}: {1}".format(loopVar + 1,resultSet[loopVar]))


"""
Code works for the sample given in the site, but shows error while submitting..
dont knwo what's wrong
"""