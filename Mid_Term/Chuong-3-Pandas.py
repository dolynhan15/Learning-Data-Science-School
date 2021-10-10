import pandas as pd
import numpy as np
#Series giong nhu DICTIONARY
data = pd.Series([0.25, 0.5, 0.75, 1.0])
#print(data.values)
#print(data.index)
data2 = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
#print(data2)
data3 = pd.Series([0.25, 0.5, 0.75, 1.0], index=[2, 5, 3, 7])
#print(data3)
population_dict = {'California': 38332521, 'Texas': 26448193,
'New York': 19651127, 'Florida': 19552860}
population = pd.Series(population_dict)
#print(population)
#print(population['California'])
pd.Series(5, index=[100, 200, 300])
pd.Series({2:'a', 1:'b', 3:'c'})
a=pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])
#print(a)

#DATAFRAME

dataFrame=pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'],index=['a', 'b', 'c'])
#print(dataFrame)
data = [{'a': i, 'b': 2 * i} for i in range(3)]
pd.DataFrame(data)
#print(pd.DataFrame(population, columns=['population']))

#INDEX
ind = pd.Index([2, 3, 5, 7, 11])
#print(ind)
#print(ind[1])
#print(ind[::2])
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])
#print(indA|indB)

data = pd.Series([0.25, 0.5, 0.75, 1.0],index=['a', 'b', 'c', 'd'])
data['e'] = 1.25
#print(list(data.items()))
#print(list(data.keys()))
data['a':'c']
print(data[0:2])
data[(data > 0.3) & (data < 0.8)]
data[['a', 'e']]
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
#print(data.loc[3]) #truy cập chỉ số tường minh
#print(data.loc[0:5]) #tham chiếu đến chỉ số tường minh 1,3,5
#print(data.iloc[1]) #vị trí index
#print(data.iloc[0:3]) #vị trí index

#DATAFRAME
area = pd.Series({'California': 423967, 'Texas': 695662, 'New York': 141297})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,'New York': 19651127})
data = pd.DataFrame({'area':area, 'pop':pop})
#print(data)
#print(data.index)
#print(data.columns)
#print(data['area'])
data['density'] = data['pop'] / data['area']
data.loc[data.density > 100, ['pop', 'density']]
print(data['Texas':'New York'])
data[1:3]
data[data.density > 100]

df = pd.read_csv('path_to_file.csv')
df.to_csv('path_to_file.csv')

area = pd.Series([10,20,30])
pop = pd.Series([20,30,40])
data = pd.DataFrame({'area':area, 'pop':pop})
print(data)