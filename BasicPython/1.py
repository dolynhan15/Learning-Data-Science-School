data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
from sklearn.utils import resample
import math
boot = resample(data, replace=True, n_samples=20)
#print('Bootstrap Sample: %s' % boot)


import pandas as pd 
a=['Tom', 'nick', 'krish', 'jack']
# intialise data of lists. 
data = {"Mean":a ,
        'Age':[20, 21, 19, 18]} 
  
# Create DataFrame 
df = pd.DataFrame(data) 
  
# Print the output. 
#print(df)
list_mean=[9,10,11,20,30]
num_bin = {10: 0, 20: 0, 30: 0, 40: 0, 50: 0}
def Mean_distribution(listmean,numbin):
    for mean in listmean:
        for key in numbin:
            if (mean <= key):
                numbin[key]+=1
                break
    return numbin
num_bin=Mean_distribution(list_mean,num_bin)
#print(num_bin)
a=list(num_bin.values())
a = [i/5 for i in a]
#print(a)
list_mean=[9,10,11,20,30]
arr_last=[10,20,30,40,50]
count=[0]*5

print(count)
for x in list_mean:
    index=0
    for i in arr_last:
        if (x<=i):
            count[index]+=1                
            break 
        index+=1     
print(count)                
                
                   