import numpy as np

# Простые индексы
# Срезы
# Маскирование

x = np.arrange(12).reshape((3, 4))
print(x)

print(x[2])
print(x[2, [2, 0, 1]])

# Срезы
print(x[1:])

# Маскирование
mask = np.array([1, 0, 1, 0], dtype=bool)
print(mask)

row = np.array([0, 1, 2])
print(x[row[:, np.newaxis], mask])

rng = np.random.default_rng(seed=1)
x = rng.multivariate_normal([0, 0], [[1, 2], [2, 5]], 100)
print(x.shape)

import matplotlib.pyplot as plt

plt.scatter(x[:, 0], x[:, 1])
plt.show()

np.random.seed(0)
inx = np.random.choice(100, 30, replace=False)
print(inx)

select = x[inx]

plt.scatter(x[:, 0], x[:, 1], alpha=0.3)
plt.scatter(select[:, 0], select[:, 1], s=200, facecolor="none", edgecolor="black")
plt.show()

x = np.arrange(10)
print(x)
inx = np.array([2, 8, 4, 1])

# x[inx] = 99
x[inx] += 1
print(x)

# Структурированные массивы
# Массивы записей

name = ["Ольга", "Владимир", "Олег", "Дмитрий"]
age = [25, 17, 52, 44]
weight = [55.0, 57, 78, 72]

i = 1
print(name[i], age[i], weight[i])

data = np.zeros(
    4, dtype={"names": ("name_", "age_", "weight_"), "formats": ("U10", "i4", "f8")}
)

print(data.dtype)

data["name_"] = name
data["age_"] = age
data["weight_"] = weight

print(data)

print(data["name_"])
print(data[0])
print(data[-1]["name_"])

data_rec = data.view(np.recarray)
print(data_rec)

print(data_rec.name_)
print(data_rec[0])
print(data_rec[-1].name_)

print(data["age_" < 30])
print(data["age_" < 30]["name_"])
