noOfCity = int(input())
city = []
cost = []
for _ in range(noOfCity) :
    city.append(input())
for _ in range(noOfCity) :
    temp = list(int,input().split())
    cost.append(temp)
visitCount = int(input())
visitCity = []
for _ in range(visitCount) :
    visitCity.append(list(map(int,input().split())))
if visitCity[0] == city[0] :
    totalCost = 0
else :
    totalCost = cost[0][city.index(visitCity[loopVar + 1])]
for loopVar in range(visitCount) :
    totalCost += cost[city.index(visitCity[loopVar])][city.index(visitCity[loopVar + 1])]
print (totalCost)