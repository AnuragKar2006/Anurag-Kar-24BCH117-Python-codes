1)
list =["hello" ,"hi", "bye" ,"please"]
set =set()
for i in list:
    set.add(i.upper())
   
print(f"The set in uppercase is {set}")

2)
import random
randomset = {random.randrange (15,45) for _ in range (10)}
print(set)
removeset= set()
print(randomset)
c=0
for i in randomset :
    if(i<30):
        c+=1
    else:
        removeset.add(i)
randomset-=removeset
print(randomset)

3)
names_set = set()
names_set.update({"Hello", "Hi", "Bye","Haha" ,"Lol"})
print("After adding names:", names_set)
names_set.discard("Bye") 
names_set.add("hey")  
print("After modifying a name:", names_set)
names_set.discard("Hello")
names_set.discard("Hi")
print("After deleting two names:", names_set)

4)
namesset = {"America", "Africa", "Boston", "Atlanta", "Bahamas", "Australia", "Bahrain"}
anames = {name for name in namesset if name.startswith("A")}
bnames = {name for name in namesset if name.startswith("B")}
print("Names starting with A:", anames)
print("Names starting with B:", bnames)