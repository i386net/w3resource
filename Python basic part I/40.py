# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# √ ((X2-X1)²+(Y2-Y1)²).


def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


p1 = (2, 4)
p2 = (4, 1)
print(round(distance(p1, p2), 2))

