import numpy as np
import pandas as pd

array=[20,4,43,92,41,55,98,32,25,69]
df = pd.DataFrame(columns=['A','B'])
for i in range(5):
    df = df.append({'A': i,'B':i}, ignore_index=True)
print(df)

a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a=a[5:10] #[5,6,7,8,9] 16 số, dư 5 số đầu, 6 số cuối
print(a)

b={'a':2,'b':3,'c':4}
for i in b:
    print(i,b[i]) #truy cập value của key

import matplotlib.pyplot as plt
#vẽ đường dọc thẳng 
plt.axvline(0.2, 0, 1, label='pyplot vertical line')
# plt.axvline(0.2, label='pyplot vertical line')
plt.legend()
plt.show()


ypoints = 0.2
#vẽ đường ngang
plt.axhline(ypoints, 0, 1, label='pyplot horizontal line')
plt.legend()
plt.show()

def make_table(n):
    part_population = (max_list - min_list) / n
    arr_part = []
    for i in range(1,n):
        arr_part.append(min_list + max_list * i)
    print(arr_part)
    str_arr_part = [''] * n
    str_arr_part[0] = str(min_list) + "-" + str(arr_part[0]-1)
    for i in range(1,n-1):
        str_arr_part[i] = str(arr_part[i-1]) + "-"+ str(arr_part[i]-1)
    str_arr_part[n-1] = str(arr_part[n-2]) + "-" + str(arr_part[n-2] + part_population) 

    count = np.zeros(n)
    list_states = [''] * n 
    for x in list_num_all:
        # murder is a key 
        for i in range(0,n-1) : 
            if x < arr_part[i]:
                # dic_murder[murder] access to the value
                count[i] += 1
                break
        if x > arr_part[n-2]:
            count[n-1] += 1
    

    arr_part.append(0)

    t = PrettyTable(['BinRange','Rate'])
    for i in range(0,n):
        t.add_row([str_arr_part[i],int(count[i])])
    print(t)
