# Minimum Öklid Mesafesinin Hesaplanması

        # Göreviniz:

# Python'da fonksiyonlar ve döngüler kavramlarını kullanarak, aşağıdaki işlemleri gerçekleştiren bir program yazmanız gerekmektedir:

# Noktaların Tanımlanması:

# ‘points’ adında bir liste oluşturun. Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir.

# Öklid Mesafesi İçin Bir Fonksiyon Yazma:

# ‘euclideanDistance’ adında bir fonksiyon tanımlayın. Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir.

# Mesafelerin Hesaplanması:

# Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. Bu mesafeleri ‘distances’ adında başka bir listede saklayın.

# Minimum Mesafenin Bulunması:

# ‘distances’ listesinden minimum mesafeyi bulun ve yazdırın.



import math

# Görev 1 / Noktaların tanımlanması 
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Görev 2 / Öklid mesafesi için bir fonksiyon yazma
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Görev 3 / Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Görev 4 / Minimum mesafenin bulunması
min_distance = min(distances)
print("Minimum Mesafe:", min_distance)
