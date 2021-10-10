class Student : 
    def __init__(self, name, age,score):
        self.name = name
        self.age = age
        self.score = score
    def __repr__(self):
        return str(dict({
            "name": self.name,
            "age": self.age,
            "score": self.score,
            
        }))


x=input("Nhap chuoi string: ")
array=[]
while x!='q':
    x = x.split(",")
    array.append(Student(name = x[0],age = x[1], score = x[2]))
    x=input("Nhap chuoi string: ")
print(array)

def myFunc(e):
  return e['year']
  

