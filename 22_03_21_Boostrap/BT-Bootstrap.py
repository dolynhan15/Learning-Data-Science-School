import math
from sklearn.utils import resample

f = open("boostrap.csv", 'r',encoding="utf-8")
listA = f.readlines()
#print(len(listA))

row=[]
i=0
num_sample_row=0
for line in listA:
    if i==0:
        i=1
        continue
    # khi có continue thì sẽ bỏ qua các câu lệnh trong vòng lặp
    x = line.split(",")
    #x là dòng string
    num_sample_row=len(x)
    for i in range(0,len(x)):
        row.append(int(x[i]))
print(row) #số phần tử trong tập mẫu
print(num_sample_row)

#tạo ra tập mẫu gồm 201 phần tử
n_size = num_sample_row * 20 + 1;
list_train=[]

for i in range(0,n_size):
    new_row = resample(row, replace=True, n_samples=num_sample_row)
    list_train.append(new_row)
#print(list_train)


def mean(y):
    sum_mean=0
    for i in y:
        sum_mean+=i
    return sum_mean/len(y)

#Median: trung vị
def median(y):
    y.sort()   
    if len(y) % 2 == 0: 
        return (y[len(y)//2]+y[len(y)//2-1])/2
    else: 
        return y[len(y)//2]

#IQR:
def IQR(y):
    y.sort()
    q50_index = len(y)//2
    q25_index = q50_index // 2
    q75_index = int(len(y)/4*3)
    return (y[q75_index] - y[q25_index])

def IQR_New(x):
    x.sort()
    Q3=np.percentile(x,75)
    Q1=np.percentile(x,25)
    return Q3-Q1

def std_deviation(y):
    #độ lệch chuẩn
    sum_std=0;
    for i in range(0,len(y)):
        sum_std+=pow((y[i]-mean(y)),2);
    return math.ceil(math.sqrt(sum_std/(len(y)-1)));
def Mean_distribution(listmean,numbin):
    for mean in listmean:
        for key in numbin:
            if (mean <= key):
                numbin[key]+=1
                break
    return numbin

list_mean = []
list_median = []
list_IQR = []
list_std_deviation = []
#print(list_train[0])
for line in list_train:
    list_mean.append(mean(line))
    list_median.append(median(line))
    list_IQR.append(IQR(line))
    list_std_deviation.append(std_deviation(line))
#print(len(list_mean))
print("")
print("--------------Confident interval of the mean Bootstrap-----------------")
total_sample = len(list_train) #tổng số mẫu : 201
print("Total sample: ",total_sample)
alpha = 0.05 
print("alpha: ",alpha)
confident_level = 100*(1-2*alpha) #độ tin cậy
print("Confident level: ",confident_level)
# confidence interval : khoảng tin cậy
list_mean.sort()
lower_bound = list_mean[int(total_sample * alpha)-1] #vị trí của phần tử thứ 10 trong listmean
print("Lower bound: ",lower_bound)
upper_bound = list_mean[int(total_sample * (1-alpha))-1]
print("upper bound: ",upper_bound)


import pandas as pd 
from prettytable import PrettyTable
# pd.options.display.max_columns = None
# pd.options.display.max_rows = None
print("--------------Bootstrap Statistic-----------------")
# intialise data of lists. 
# data1 = {"Mean":list_mean,
#         "Median":list_median,
#         "Inter quartile range":list_IQR,
#         "Std deviation":list_std_deviation}   
# # Create DataFrame 
# df1 = pd.DataFrame(data1) 
# print(df1) 

t = PrettyTable(['STT','Mean', 'Median','IQR', 'Standard Division'])
for i in range(0, n_size):
    t.add_row([i+1,list_mean[i], list_median[i], list_IQR[i],list_std_deviation[i]])
print(t)

num_bin = {10: 0, 20: 0, 30: 0, 40: 0, 50: 0, 60:0, 70:0, 80:0, 90:0, 100:0}
num_bin=Mean_distribution(list_mean,num_bin)
list_bin = list(num_bin.keys())
list_frequency = list(num_bin.values())
list_probability = [round(i/total_sample,2) for i in list_frequency]
# số 2 là lấy 2 chữ số thập phân

# data2 = {"Bin":list_bin,
#         "Frequency":list_frequency,
#         "Probability":list_probability}  
# df2 = pd.DataFrame(data2) 

# new_row = ["SUM",total_sample,1]
# df2 = df2.append(pd.Series(new_row, index = df2.columns), ignore_index=True)
# print("")
# print("--------------Mean distribution-----------------")
# print(df2.to_string(index=False))


print("--------------Mean distribution-----------------")
df = PrettyTable(['Bin','Frequency', 'Probability'])
# df = pd.DataFrame(columns=['Bin','Frequency', 'Probability'])
i = 0 
for key in num_bin:
    # df = df.append({'Bin': key,'Frequency':bin_number[key],'Probability':probability[i]}, ignore_index=True)
    df.add_row([key,num_bin[key], list_probability[i]])
    i += 1
df.add_row(["SUM",total_sample,1])
# df = df.append({'Bin': "SUM",'Frequency':total_sample,'Probability':1}, ignore_index=True)
print(df)
# print(df)


import matplotlib.pyplot as plt 
import numpy as np
# x axis values 
#tạo mảng từ 0->100 cách đều nhau 10
x = np.arange(0,100,10)
plt.plot(x, list_probability) 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('My first graph!') 
plt.bar(x, list_probability, color='purple', width = 5)  #vẽ khối trụ

# plt.axvline(lower_bound, linestyle = 'dotted',color='green',label='pyplot vertical line')
plt.axvline(lower_bound, color='green',label='pyplot vertical line')
plt.axvline(upper_bound, color='green',label='pyplot vertical line')
# function to show the plot 
plt.show() 