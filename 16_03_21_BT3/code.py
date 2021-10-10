import math
rate = []
population = []
sum_mean=sum_population=sum_weight_mean=sum_trimmed_mean=0;
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
print(rate)
for i in rate:
    sum_mean=sum_mean+i

#mean: Giá trị trung bình
mean_rate = sum_mean/len(rate)
print("mean_rate = ",mean_rate)

m=0
sum_weight=0
while (m<len(rate)):
    sum_weight_mean += population[m]*rate[m]
    sum_weight += population[m]
    m += 1
#weight_mean: giá trị trung bình có trọng số
weight_mean=sum_weight_mean/sum_weight
print("weight_mean = ",weight_mean)

rate.sort()
rate2=rate[5:45]
for i in rate2:
    sum_trimmed_mean=sum_trimmed_mean+i
#trimmed_mean: Giá trị trung bình tinh gọn
trimmed_mean=sum_trimmed_mean/len(rate2)
print("trimmed_mean = ",trimmed_mean)

for i in population:
    sum_population=sum_population+i

#mean: Giá trị trung bình
mean_population = sum_population/len(population)
#MAD: độ lệch tuyệt đối trung bình (x-x(Trung bình))/n
sum_MAD=0;
for i in range(0,len(population)):
    sum_MAD+=abs(population[i]-mean_population);
MAD=sum_MAD/len(population);

print("MAD = ",MAD);
#Độ lệch chuẩn(standard deviation) = căn(phương sai(variance))
#phương sai(variance)=(x(i)-x(ngang))^2/(n-1)
sum_Variance=0;
for i in range(0,len(population)):
    sum_Variance+=pow((population[i]-mean_population),2);
Variance=math.sqrt(sum_Variance/(len(population)-1));
print("Variance = ",Variance);
