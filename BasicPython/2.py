import numpy as np

print(np.empty([2,3,3]))


numeric_strings = np.array(['1.25','-9.6', '42'], dtype=np.string_)
print(numeric_strings.astype(float))

print(np.arange(10))

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(names)
print(data)
print(names=='Bob')
print(data[names=='Bob']) #in vi tri True cua Bob
print("//")
print(data[names == 'Bob', 2:])
print("//")
print(data[names == 'Bob', 3])
print("//")
data[data < 0] = 0
print(data)
print("///////")
names = np.array(['Tuan', 'Phuong', 'Khoi', 'Hieu', 'Duy'
, 'Thang', 'Duc'])
print(names)
print(names[[0,5,4]])
print("///////")
arr = np.arange(32).reshape((8, 4))
print(arr)
print("----")
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print("----")
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])