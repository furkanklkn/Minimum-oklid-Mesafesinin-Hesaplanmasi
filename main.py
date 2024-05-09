import math

# Adım 1: Noktaların Tanımlanması
points = [(2, 3), (5, 7), (1, 9), (4, 6), (8, 2)]

# Adım 2: Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Adım 3: Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Adım 4: Minimum Mesafenin Bulunması
min_distance = min(distances)
print("Minimum Mesafe:", min_distance)
