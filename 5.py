# Pandas
# Series
# DataFrame
# Index
import numpy as np
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5])
print(data)

print(data.values)
print(type(data.values))

print(data.index)
print(type(data.index))

print(data[1])
print(data[1:3])

data = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(data)

# Списки
data = pd.Series([1, 2, 3, 4, 5])
print(data)

data = pd.Series(5, index=[10, 20, 30])
print(data)

# Словари
data = pd.Series({"a": 1, "b": 2, "c": 3})
print(data)

data = pd.Series({"a": 1, "b": 2, "c": 3}, index=["a", "b", "c", "d", "e"])
print(data)

# Nan
data = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
data[2] = np.nan
print(data)

# Index - способ сослаться (reference) на данные в Series или в DataFrame
index = pd.Index([1, 2, 3, 4, 5])
print(index)

print(index[1])
print(index[1:3])

# NumPy
# Индексация arr[1, 2]
# Срезы arr[:, 1:4]
# Маскирование arr[arr > 2]

data = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(data)

print(data["a"])
print("a" in data)
print("a1" in data)

print(list(data.items()))
data["a"] = 99
print(data)

data["a1"] = 909
print(data)

print(data["c":"a1"])

print(data[2:4])

print(data[data > 2])

print(data[["c", "a1"]])

print(data.iloc[2:4])

# Атрибуты-индексаторы
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40,
    "E": 50,
}

data_dict1 = pd.Series(dict1)
print(data_dict1)

dict2 = {
    "A": 11,
    "B": 22,
    "C": 33,
    "D": 44,
    "E": 55,
}

data_dict2 = pd.Series(dict2)
print(data_dict2)

df = pd.DataFrame({"dict_01": data_dict1, "dict_02": data_dict2})
print(df)

print(df.dict_01)
print(df["dict_01"])

df["new"] = df["dict_01"]
print(df)

df["new_1"] = df["dict_01"] / df["dict_02"]
print(df)

rng = np.random.default_rng(1)
s = pd.Series(rng.integer(10, 100, 10))
print(s)

print(np.exp(s))

df = pd.DataFrame(rng.integers(10, 100, (10, 5)), columns=list("ABCDE"))
print(df)
