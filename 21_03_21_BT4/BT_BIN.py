import numpy as np 
from prettytable import PrettyTable

class Murder : 
    def __init__(self,state,population, murderRate,abbreviation):
        self.state = state
        self.population = population
        self.murderRate = murderRate
        self.abbreviation = abbreviation
    def __repr__(self):
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
    dic_murder[x[1]] =  Murder(state = x[0], population = float(x[1]), murderRate= float(x[2]), abbreviation=x[3].replace('\n',''))

population = []
for murder in dic_murder:
    population.append(dic_murder[murder].population)
min_population = min(population)
max_population = max(population)

def make_table(n):
    part_population = (max_population - min_population) / n
    arr_part = []
    for i in range(1,n):
        arr_part.append(min_population + part_population * i)
    print(arr_part)
    str_arr_part = [''] * n
    str_arr_part[0] = str(min_population) + "-" + str(arr_part[0]-1)
    for i in range(1,n-1):
        str_arr_part[i] = str(arr_part[i-1]) + "-"+ str(arr_part[i]-1)
    str_arr_part[n-1] = str(arr_part[n-2]) + "-" + str(arr_part[n-2] + part_population) 

    count = np.zeros(n)
    list_states = [''] * n 
    for murder in dic_murder:
        # murder is a key 
        for i in range(0,n-1) : 
            if dic_murder[murder].population < arr_part[i]:
                # dic_murder[murder] access to the value
                count[i] += 1
                if (dic_murder[murder].abbreviation not in list_states[i]):
                    list_states[i] += dic_murder[murder].abbreviation + ","
                break
        if dic_murder[murder].population > arr_part[n-2]:
            count[n-1] += 1
            if (dic_murder[murder].abbreviation not in list_states[n-1]):
                list_states[n-1] += dic_murder[murder].abbreviation + ","  
    

    arr_part.append(0)

    t = PrettyTable(['BinNumber', 'BinRange','Count','States'])
    for i in range(0,n):
        t.add_row([i+1,str_arr_part[i],int(count[i]),list_states[i].replace('"','')])
    print(t)

make_table(10)
