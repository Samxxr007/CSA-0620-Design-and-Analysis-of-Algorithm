import math

points = [(1,2), (4,5), (7,8), (3,1)]

d = math.inf

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = math.sqrt((points[i][0]-points[j][0])**2 +
                         (points[i][1]-points[j][1])**2)
        if dist < d:
            d = dist
            pair = (points[i], points[j])

print("Closest Pair =", pair)
print("Distance =", d)