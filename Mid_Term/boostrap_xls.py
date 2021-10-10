import pandas as pd
import numpy as np
from sklearn.utils import resample
from prettytable import PrettyTable
import math

# đoạn lệnh này giúp cho mình muốn đọc theo cụm ô trong file
# ví dụ như boostrap dữ liệu mình cần lấy là từ ô B6 => K8
# nrows là số dòng muốn lấy 
# skiprows là số dòng bỏ qua tính từ dòng đầu tiên trong excel

data_excel = pd.read_excel('boostrap.xls', usecols='B:K', nrows=3, skiprows=5, header=None)
#data_excel = pd.read_csv('boostrap.csv')
print(data_excel)

df = pd.DataFrame(data_excel)
rows = df.shape[0] # số hàng 

list_all = []
values = []

for i in range(0,rows):
    list_row = []
    for j in range(1,11):    # sử dụng đối với file excel
    #for j in range(0,10):   # sử dụng đối với file csv
        # tại sao là 6 tới 11 ? Ở cái lệnh print(data_excel) dữ liệu hiển thị ra là cột 6 => 10
        list_row.append(df.loc[i][j])
        values.append(df.loc[i][j])
    list_all.append(list_row)


#print(list_all)
#print(list_all[0]) # print first resample tests
n_size = int(len(list_all[0]) * 20) + 1     # 201 mẫu 

train_all = []

# tạo tập mẫu để train 
for i in range(0,n_size):
    train = resample(values, n_samples=len(list_all[0]))
    train_all.append(train)

print(len(train_all))

bin_number = {10: 0, 20: 0, 30: 0, 40: 0, 50: 0, 60:0, 70:0, 80:0, 90:0, 100:0}

def mean(x):
    sum_mean = 0 
    for i in x : 
        sum_mean += i 
    mean = sum_mean / len(x) # end of mean

    # tính thêm vào phần bin number ở trên 
    # ở đây mean tính theo từng dòng trong dữ liệu cho nên nó lặp lại liên tục chơ không phải chỉ chạy 1 lần
    for key in bin_number:
        if mean <= key : 
            bin_number[key]  += 1
            break
    return mean

def median(x):
    x.sort()
    return (x[int(len(x)/2)-1] + x[int(len(x)/2)]) / 2

def IQR_learn(x):
    x.sort()
    Q1_index = int(len(x)/2)
    Q1_index = int(Q1_index // 2)
    Q3_index = int(Q1_index + int(len(x))/2)
    return (x[Q3_index] - x[Q1_index])

def IQR_percentlive(x):
    Q3_new = np.percentile(x,75)
    Q1_new = np.percentile(x,25)
    return (Q3_new-Q1_new)
    
def standard_division(x, mean_x) : # giá trị trung bình bình phương
    sum_standard = 0
    for i in x : 
        sum_standard += pow(i - mean_x,2)
    sum_standard /= len(x) - 1
    standard = math.sqrt(sum_standard)
    standard = math.ceil(standard * 100) / 100.0    # làm tròn 
    return standard
    
list_mean = []
list_median = []
list_iqr_learn = []
list_standard = []

for list_row in train_all: 
    list_mean.append(mean(list_row))
    list_median.append(median(list_row))
    list_iqr_learn.append(IQR_learn(list_row))
    list_standard.append(standard_division(list_row, list_mean[-1]))


t = PrettyTable(['STT','Mean', 'Median','IQR', 'Standard Division'])
for i in range(0, n_size):
    t.add_row([i+1,list_mean[i], list_median[i], list_iqr_learn[i],list_standard[i]])
print(t)

total_sample = len(train_all)
alpha = 0.05
confident_level = 100*(1-2*alpha)

list_mean.sort()
lower_bond = list_mean[int(total_sample*alpha) - 1]
print(lower_bond)
upper_bond = list_mean[int(total_sample*(1-alpha)) - 1]
print(upper_bond)

probability = []
frequency = []
for key in bin_number:
    prob = bin_number[key] / total_sample
    prob = math.ceil(prob * 100) / 100.0
    frequency.append(bin_number[key])
    probability.append(prob)

z = PrettyTable(['Bin','Frequency', 'Probability'])
i = 0 
for key in bin_number:
    z.add_row([key,bin_number[key], probability[i]])
    i += 1
z.add_row(["SUM",total_sample,1])
print(z)


import matplotlib.pyplot as plt 
# x axis values 
x = np.arange(0,100,10)
plt.plot(x, probability, color='red') # vẽ đường nối các điểm 
plt.xlabel('Bin Number') 
plt.ylabel('Probability') 
plt.title('Mean Boostrap') 
plt.bar(x, probability, color='black', width = 6)  # vẽ các thanh bar 
# function to show the plot 
plt.show() 