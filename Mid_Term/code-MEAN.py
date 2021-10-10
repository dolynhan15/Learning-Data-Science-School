import math
rate = []
population = []
sum_population=0;
f = open("state.csv", 'r',encoding="unicode_escape")
listA = f.readlines()

i=0
for line in listA:
    if i==0:
        i=1
        continue
    # khi có continue thì sẽ bỏ qua các câu lệnh trong vòng lặp
    x = line.split(",")
    rate.append(float(x[2])) # add to list 
    population.append(int(x[1]))
# print(rate)

#mean: Giá trị trung bình
def mean(list_X):
    sum_mean=0
    for i in list_X:
        sum_mean=sum_mean+i        
    mean = sum_mean/len(list_X)
    return mean

#weight_mean: giá trị trung bình có trọng số
def weight_mean(list_population,list_rate):
    m=0
    sum_weight=sum_weight_mean=0
    for m in range(0,len(list_rate)):
    # while (m<len(list_rate)):
        sum_weight_mean += list_population[m]*list_rate[m]
        sum_weight += list_population[m]
        m += 1
    weight_mean=sum_weight_mean/sum_weight
    return weight_mean

#trimmed_mean: Giá trị trung bình tinh gọn trừ đi 5 gt đầu , 5 gt cuối
def trimmed_mean(list_rate):
    sum_trimmed_mean=0
    rate.sort()
    rate2=rate[5:45]
    for i in rate2:
        sum_trimmed_mean=sum_trimmed_mean+i    
    trimmed_mean=sum_trimmed_mean/len(rate2)
    return trimmed_mean

#MAD: độ lệch tuyệt đối trung bình abs(x-x(Trung bình))/n
def MAD(list_population):
    sum_MAD=0;
    for i in range(0,len(list_population)):
        sum_MAD+=abs(list_population[i]-mean(list_population));
    MAD=sum_MAD/len(list_population);
    return MAD   
    
#Độ lệch chuẩn(standard deviation) = căn(phương sai(variance))
#phương sai(variance)=(x(i)-x(ngang))^2/(n-1)
def Standard_deviation(list_population):
    sum_Variance=0;
    for i in range(0,len(list_population)):
        sum_Variance+=pow((list_population[i]-mean(list_population)),2)
    Variance=sum_Variance/(len(list_population)-1)
    Standard_deviation=math.sqrt(Variance)
    return Standard_deviation
    


print("Mean_rate = ",mean(rate))
print("weight_mean = ",weight_mean(population,rate))
print("Trimmed_mean = ",trimmed_mean(rate))
print("MAD = ",MAD(population))
print("Standard_deviation = ",Standard_deviation(population))