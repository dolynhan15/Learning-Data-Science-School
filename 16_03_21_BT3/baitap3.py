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
# lưu ý là encoding utf 8 sẽ gây ra lỗi còn unicode_escapse sẽ ko có lỗi 
listoflines = f.readlines()
i = 0
for line in listoflines:
    #print(line) 
    if i == 0 : 
        i = 1
        continue
    count += 1 
    x = line.split(",")
    murder.append(Murder(state = x[0], population = float(x[1]), murderRate= float(x[2]), abbreviation=x[3])) # add to list 
    dic_murder[x[1]] =  Murder(state = x[0], population = float(x[1]), murderRate= float(x[2]), abbreviation=x[3])

sum_mean = sum_weigth_mean= sum_weight= 0

murderRate = []
for murder in dic_murder:
    sum_mean += dic_murder[murder].murderRate
    sum_weigth_mean += dic_murder[murder].murderRate * dic_murder[murder].population
    sum_weight += dic_murder[murder].population
    murderRate.append(dic_murder[murder].murderRate)

murderRate.sort()

print(murderRate)
murder2 = murderRate[5:45]
sum_murder2 = 0
for murder in murder2 : 
    sum_murder2 += murder
print("trimmed = " ,sum_murder2 / (count - 10)) 
print("median = ", murderRate[int(count / 2)])

mean = sum_mean / count
print(sum_mean)
print("mean = ", mean) 
print("weight_mean =", sum_weigth_mean / sum_weight)