
# a)
import numpy as np
import math
data1=np.random.normal(100,20,1000)
data2=np.random.normal(50,10,1000)
# print("Data1",data1)
# print("data2",data2)

# b)
data3=data1+data2
print("data3",data3)

# c)
def mean(list_X):
    sum_mean=0
    for i in list_X:
        sum_mean=sum_mean+i        
    mean = sum_mean/len(list_X)
    return mean

print("Trung bình mẫu data3",mean(data3))
print("Trung bình mẫu data1",mean(data1))

def Standard_deviation(list_population):
    sum_Variance=0;
    for i in range(0,len(list_population)):
        sum_Variance+=pow((list_population[i]-mean(list_population)),2)
    Variance=sum_Variance/(len(list_population)-1)
    Standard_deviation=math.sqrt(Variance)
    return Standard_deviation


print("Độ lệch chuẩn mẫu data3",Standard_deviation(data3))
print("Độ lệch chuẩn mẫu data1",Standard_deviation(data1))