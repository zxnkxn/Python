import array
import sys

import numpy as np

print(np.__version__)

# В Python динамическая типизация
x = 1
print(type(x))

x = "Hello"
print(type(x))

lst = [True, "3", 9, 6.5]
print([type(i) for i in lst])

# 88 байт
print(sys.getsizeof(lst))

lst1 = []
print(type(lst1))
# 56 байт
print(sys.getsizeof(lst1))

a1 = array.array("i", [])
print(type(a1))
# 80 байт
print(sys.getsizeof(a1))

a1 = array.array("i", [1])
# 84 байта
print(sys.getsizeof(a1))

a1 = array.array("i", [1, 2])
# 88 байт
print(sys.getsizeof(a1))

# Numpy & Python array - массивы хранят элементы одного типа

# Создание из списка
lst = [1, 2, 3, 4, 5]
a = np.array(lst)
print(a)
print(type(a))
print("List Python:", sys.getsizeof(lst))
ap = array.array("i", lst)
print("Array Python:", sys.getsizeof(ap))
print("Numpy array:", sys.getsizeof(a))

# Повышающее приведение типа
a = np.array([1, 2.1, 3, 4, 5])
print(a)
print("Numpy array:", sys.getsizeof(a))

# Можем явно задать тип данных
a = np.array([1, 2.1, 3, 4, 5], dtype=np.int32)
print(a)
print("Numpy array:", sys.getsizeof(a))

# Одномерные массивы
a = np.array([1, 2, 3, 4, 5])
print(a)
print("Numpy array:", sys.getsizeof(a))

# Многомерные массивы
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print("Numpy array:", sys.getsizeof(a))

# Создание массива из нулей и единиц
a = np.zeros((2, 3))
print(a)
print("Numpy array:", sys.getsizeof(a))

a = np.ones((2, 3))
print(a)
print("Numpy array:", sys.getsizeof(a))

# Многомерные массивы из единиц
a = np.ones((2, 3))
print(a)
print("Numpy array:", sys.getsizeof(a))

# Можем задать своё значение для массива
a = np.full((2, 3), 1)
print(a)
print("Numpy array:", sys.getsizeof(a))

# Линейная последовательность чисел
a = np.arange(10)
print(a)
print("Numpy array:", sys.getsizeof(a))

# В интервале с одинаковыми промежутками
a = np.linspace(0, 10, 11)
print(a)
print("Numpy array:", sys.getsizeof(a))

# Равномерное распределение от 0 до 1
a = np.random.rand(10)
print(a)
print("Numpy array:", sys.getsizeof(a))

# Нормальное распределение от 0 до 1
a = np.random.randn(10)
print(a)
print("Numpy array:", sys.getsizeof(a))

# Равномерное распределение (randint)
a = np.random.randint(0, 10, 10)
print(a)
print("Numpy array:", sys.getsizeof(a))

# Единичная матрица
a = np.eye(3)
print(a)
print("Numpy array:", sys.getsizeof(a))

# Типы данных
a = np.zeros((2, 3), dtype=np.int16)
print(a)
print("Numpy array:", sys.getsizeof(a))

a = np.zeros((2, 3), dtype=np.int32)
print(a)
print("Numpy array:", sys.getsizeof(a))

a = np.zeros((2, 3), dtype=np.int64)
print(a)
print("Numpy array:", sys.getsizeof(a))

a = np.zeros((2, 3), dtype=np.float32)
print(a)
print("Numpy array:", sys.getsizeof(a))

a = np.zeros((2, 3), dtype=np.float64)
print(a)
print("Numpy array:", sys.getsizeof(a))

# Numerical Python = NumPy
# - атрибуты массивов
# - индексация
# - срезы
# - изменение формы
# - объединение и разбиение

# Атрибуты массивов
a = np.array([1, 2, 3, 4, 5])
print(a.shape)
print(a.ndim)
print(a.size)

# Индексация
a = np.array([1, 2, 3, 4, 5])
print(a[0])
print(a[-1])

# Срезы
a = np.array([1, 2, 3, 4, 5])
print(a[1:3])

# Изменение формы
a = np.array([1, 2, 3, 4, 5])
print(a.reshape(5, 1))

# Объединение и разбиение
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
print(np.concatenate((a, b)))
print(np.split(a, 2))
