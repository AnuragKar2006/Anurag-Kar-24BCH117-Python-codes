1)
list = ["trisha" ,"maya", ("jai" ,"veeru"),"jaya"]
a = len(list)
c=0
d=0
for i in list:
    if isinstance(i,tuple):
        c+=len(i)
    else:
        d+=1
print(f"The number of boys are {c}")
print(f"The number of girls are {d}")

2)
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

3)
date1 =(15,11,2005)
date2=(25,2,2025)
day1,month1,year1=date1
a=day1
print(a)

4)
list =[("noodles" ,300) , ("dabeli" , 30) ,("vadapav" ,40) ,("veg combo" ,350)]
sortedlist=[]

while list:
    maxprice=list[0]
    for i in list:
        if(i[1]>maxprice[1]):
            maxprice=i
    sortedlist.append(maxprice)
    list.remove(maxprice)
for i in sortedlist:
    print(i)

5)
list = [(), (1, 2), (), (3,), (4, 5, 6), ()]
filteredlist = []
for t in list:
    if t != ():
        filteredlist.append(t)

print("Filtered list:", filteredlist)

6)
tuple = (1, 2, 3, 4)
newtuple = ()


for i in range(len(tuple)):
    if i == 1: 
        newtuple += (20,)
    else:
        tuple += (tuple[i],)

print("Modified tuple:", tuple)

7)
tuple = (1, 2, 3, 4)
newtuple = ()


for i in range(len(tuple)):
    if i == 2:  
        continue
    newtuple += (tuple[i],)

print("Tuple after deletion:", newtuple)


































