import numpy as np

# Тема 2. Слияние и разбиение массивов
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
print(np.concatenate((a, b)))

# Двумерные массивы
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate((a, b)))

# vstack и hstack
print(np.vstack((a, b)))
print(np.hstack((a, b)))

# dstack
print(np.dstack((a, b)))

# Разбиение массивов
print(np.split(a, 2))

# Разбиение массивов по столбцам
print(np.split(a, 2, axis=1))

# vsplit и hsplit
print(np.vsplit(a, 2))
print(np.hsplit(a, 2))

# dsplit
print(np.dsplit(a, 2))

# Универсальные функции
# Арифметические операции
x = np.arrange(5)
print(x)

print(x + 1)
print(x - 1)
print(x * 2)
print(x / 2)

print(np.add(x, 1))
print(np.subtract(x, 1))
print(np.multiply(x, 2))
print(np.divide(x, 2))

x = np.arange(-5, 5)

print(abs(x))
print(np.abs(x))

# Комплексные числа
x = np.array([3 + 4j, 4 - 3j])
print(abs(x))
print(np.abs(x))

# Тригонометрические функции
x = np.array([0, np.pi / 2, np.pi])
print(np.sin(x))
print(np.cos(x))

# Логарифмические функции
x = np.array([1, 2, 3, 4, 5])
print(np.log(x))
print(np.log2(x))
print(np.log10(x))

# Агрегирование

np.random.seed(1)
s = np.random.random(100)
print(sum(s))
print(np.sum(s))

# Минимум / максимум
print(min(s))
print(max(s))

print(np.min(s))
print(np.max(s))

# Среднее значение
print(np.mean(s))

# Медиана
print(np.median(s))

# std, var, argmin, argmax, percentile, any, all
print(np.std(s))
print(np.var(s))
print(np.argmin(s))
print(np.argmax(s))
print(np.percentile(s, 50))
print(np.any(s))
print(np.all(s))

# Транслирование (broadcasting)
# Бинарные операции с массивами разных форм
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)
# 5 -> np.array([5, 5, 5])
print(x + 5)
