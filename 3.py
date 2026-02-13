import numpy as np

# Правила транслирования
a = np.ones((2, 3))
b = np.arrange(3)

print(a)
print(b)

# print(a.shape, b.shape)

c = a + b
print(c)
print(c.shape)

# Центрирование массивов
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1])
print(a)

aMean = a.mean()
print(aMean)

print(a.shape)
print(aMean.shape)

aCentered = a - aMean
print(aCentered)

import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

z = np.sin(x) * y

print(z)

plt.imshow(z)
plt.show()

# Маскирование

x = np.arrange(1, 6)
a = x < 3
print(a)

# Сколько элементов имеют значение меньше 6

print(np.count_nonzero(x < 6))

# Наложение маски

x = np.arrange(1, 6)
a = x < 3
print(x[a])

# & |
a = x < 3
b = x > 3
print(a & b)
print(a | b)

# Векторизированная / прихотливая (fancy) индексация

a = np.arrange(1, 6)
print(a[0], a[1], a[2], a[3], a[4])
print(a[[0, 1, 2, 3, 4]])
