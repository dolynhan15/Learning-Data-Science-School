import pandas as pd
df = pd.read_excel('Book1.xlsx')
#df = pd.read_csv('Check.csv', encoding='unicode_escape')
print(df)
print(df.shape[1])
rows = df.shape[0]
for i in range(0,rows):
    print(df.loc[i][2])
dict_student = dict()
stt=[]
name=[]
date=[]
class_study=[]
#print(df['STT']) // in ra gia tri cua cot va kieu du lieu
#print(df.columns[0]) // in ra ten cac cot
#print(df['STT'].values) // in ra gia tri cua cot

data = pd.DataFrame({'STT':df['STT'].values,'NAME':pd.Series(df['Name']),'DATE OF BIRTH':df['Date of birth'],'CLASS':df['Class']})
print(data)
print(type(df))
print(type(data))

area = pd.Series([10,20,30])
pop = pd.Series([20,30,40])
print(area)
data = pd.DataFrame({'area':area, 'pop':pop})
print(data)