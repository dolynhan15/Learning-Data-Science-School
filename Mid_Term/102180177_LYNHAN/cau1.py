from random import random

#a)
list_all=[]
list_num=[]
for i in range(0,1001):
    x=random()
    list_all.append(x)

list_num=list_all[0:10]
# print(list_num)
for i in list_num:
    print(i)

    
list_num_all=[]
for i in list_all:
    list_num_all.append(i)
# print(list_num_all)
#b)
print("Min = ",min(list_num_all))
print("Max = ",max(list_num_all))
def mean(y):
    sum_mean=0
    for i in y:
        sum_mean+=i
    return sum_mean/len(y)
print("Mean = ",mean(list_num_all))

def median(y):
    y.sort()   
    if len(y) % 2 == 0: 
        return (y[len(y)//2]+y[len(y)//2-1])/2
    else: 
        return y[len(y)//2]
print("Median = ",median(list_num_all))
max_list=max(list_num_all)
min_list=min(list_num_all)
distance = (max_list-min_list)/20
print("Range = ",max_list-min_list)
# print(list_num_all)

#c)

# print(max_list)
# print(min_list)
# print(distance)
arr_first = []
arr_last = []
for i in range(1,21):
    if (i==20):
        arr_last.append(max_list)
    else:
        # arr_last.append((min_list+distance-1)+(i-1)*distance)
        arr_last.append(min_list+distance-0.01+(i-1)*distance)
    arr_first.append(min_list+(i-1)*distance)          
# print("arr_first")
# print(arr_first)

# print("arr_last")
# print(arr_last)
str_arr_part = [''] * 20
for i in range(0,len(arr_first)):
    str_arr_part[i] = str(arr_first[i]) + "-" + str(arr_last[i])
# print(str_arr_part)

count=[0]*20
for x in list_num_all:
    index=0
    for i in arr_last:
        if (x<=i):
            count[index]+=1                
            break 
        index+=1   


from prettytable import PrettyTable
t = PrettyTable(['BinRange','Rate'])
for i in range(0,len(arr_last)):
    t.add_row([str_arr_part[i],int(count[i])])
print(t)

#d)
print("Bảng tần suất phân bố đều")