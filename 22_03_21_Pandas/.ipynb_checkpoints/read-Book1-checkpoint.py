import pandas as pd
class Student : 
    def __init__(self, id, name,date_of_birth, class_study):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.class_study = class_study
    def __repr__(self):
        return str(dict({
            "id": self.id,
            "name": self.name,
        }))
students = []
f = open("Check.csv", 'r',encoding="unicode_escape")
listoflines = f.readlines()
for line in listoflines:
    #print(line) 
    x = line.split(",")
    students.append(Student(id = x[1],name = x[2], date_of_birth = x[3] , class_study = x[4])) # add to list 
    #dic_students[x[1]] =  Student(id = x[1],name = x[2], date_of_birth = x[3] , class_study = x[4]) # add to dictionary 

print(students)
#for x in students:
 #   series_id = pd.Series()