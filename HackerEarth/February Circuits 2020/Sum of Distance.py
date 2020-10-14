from math import sin, cos
import numpy

count = int(input())
all_points = list(map(int, input().split()))

distance = 0
for item in range(1, int(pow(2, count))):
    # print (bin(item))
    binary = list(str(bin(item)))
    if binary.count("1") == 2:
        binary.pop(0)
        binary.pop(0)
        if len(binary) != count:
            binary = ["0"] * (count - len(binary)) + binary
        # get all index of appearance of "1"
        point_set = list(numpy.where(numpy.array(binary) == "1")[0])
        distance += sin(all_points[point_set[0]] + all_points[point_set[1]]) * cos(
            all_points[point_set[0]] - all_points[point_set[1]]
        )

print(round(distance, 2))

