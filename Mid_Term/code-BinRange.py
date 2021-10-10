from prettytable import PrettyTable
class Murder : 
    def __init__(self,state,population, murderRate,abbreviation):
        self.state = state
        self.population = population
        self.murderRate = murderRate
        self.abbreviation = abbreviation
    def __repr__(self):  # hàm định nghĩa dùng khi mà sử dụng lệnh print
        return str(dict({
            "state": self.state,
            "population" : self.population,
            "murderRate" : self.murderRate,
            "abbreviation": self.abbreviation,
        }))

murder = []
dic_murder = dict()
count = 0
f = open("state.csv", 'r',encoding="utf-8")

listoflines = f.readlines()
i = 0
for line in listoflines:
    if i == 0 : 
        i = 1
        continue
    count += 1 
    x = line.split(",") 
    # print(x)
    dic_murder[x[1]] =  Murder(state = x[0], population = float(x[1]), murderRate= float(x[2]), abbreviation=x[3].replace('\n',''))

population = []
for murder in dic_murder:
    population.append(dic_murder[murder].population)
min_population = min(population)
max_population = max(population)
# print(min_population)
distance = (max_population-min_population)/10
# print(distance)

arr_first = []
arr_last = []
for i in range(1,11):
    if (i==10):
        arr_last.append(max_population)
    else:
        arr_last.append((min_population+distance-1)+(i-1)*distance)
    arr_first.append(min_population+(i-1)*distance)          

# print(arr_last)
# print(arr_first)
str_arr_part = [''] * 10
for i in range(0,len(arr_first)):
    str_arr_part[i] = str(arr_first[i]) + "-" + str(arr_last[i])
# print(str_arr_part)

list_states = [''] * 10 
count=[0]*10

for murder in dic_murder:
    index=0
    for i in arr_last:
        if (dic_murder[murder].population<=i):
            count[index]+=1                
            if (dic_murder[murder].abbreviation not in list_states[index]):
                    list_states[index] += dic_murder[murder].abbreviation + ","
            break 
        index+=1   

# print(count)  
print(list_states)
t = PrettyTable(['BinNumber', 'BinRange','Count','States'])
for i in range(0,10):
    t.add_row([i+1,str_arr_part[i],int(count[i]),list_states[i].replace('"','')])
print(t)