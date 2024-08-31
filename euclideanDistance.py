import math

x1, y1 = map(int, input("Birinci nokta için x ve y değerlerini girin (x y formatında): ").split())
x2, y2 = map(int, input("İkinci nokta için x ve y değerlerini girin (x y formatında): ").split())


def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

point1 = (x1, y1)
point2 = (x2, y2)
distance = euclideanDistance(point1, point2)


print("İki nokta arasındaki minimum mesafe:", distance)
