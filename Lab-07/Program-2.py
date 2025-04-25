list = [("24BCH117","Hello",18),("24BCH124","Hi",20),("24BCH134","Bye",19)]
rollnum =[]
age=[]
name=[]
for i in list:
    rollnum.append(i[0])
    age.append(i[2])
    name.append(i[1])
print(f"Roll number : {rollnum}")
print(f"Name : {name}")
print(f"Age:{age}")
