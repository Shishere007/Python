def togglebit( n):
	if (n == 0): 
		return 1	
	i = n  
	n = n|(n >> 1) 
	n |= n >> 2
	n |= n >> 4
	n |= n >> 8
	n |= n >> 16
	return i ^ n 
	 
def XNOR( num1, num2):	
	if (num1 < num2): 
		temp = num1 
		num1 = num2 
		num2 = temp 
	num1 = togglebit(num1)	
	return num1 ^ num2
testCase = int(input())
while testCase > 0 :
    testCase -= 1    
    numbers = list(map(int,input().split()))
    a = numbers[0]
    b = numbers[1]
    n = numbers[2]
    if n % 3 == 0 :
        pos = 3 - 1
    else :
        pos = (n % 3) - 1
    xorList = [a,b]
    xnorList = [a,b]
    for loopVar in range(3,20) :
        xorList.append(xorList[loopVar - 3] ^ xorList[loopVar - 2])
        xnorList.append(XNOR(xnorList[loopVar - 3], xnorList[loopVar - 2]))
    print (xorList)
    print (xnorList)
    print (max(xorList[pos],xnorList[pos]))