
no_of_days = int(input())
toffee_count = 0
pi = 22.0 / 7

def area(radius) :
    return 2 * radius *pi

def distance_possible(x) :
    return 100 * x

for _ in range(no_of_days) :
    data = input().split()
    if area(int(data[0])) < distance_possible(int(data[1])) :
        toffee_count += 1
    
print (toffee_count)
    

# index 0 = radius
# index 1 = amount of horlicks


