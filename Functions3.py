1)
def fun():
    print("This is function fun()")

def disp():
    print("This is function disp()")

def msg():
    print("This is function msg()")


functions = [fun, disp, msg]


for func in functions:
    func()

2)
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]


result = list(map(lambda x, y: x + y, list1, list2))


print(result)

3)
import random
list =[random.randrange(-15,15) for _ in range (10)]
squared =[]
for i in list:
    f =i**2
    squared.append(f)
print(squared)

4)
lst = ['madam','Python',"malayalam","12321"]
new_lst=[]
for char in lst:
    str=char[::-1]
    if(str==char):
        new_lst.append(char)
print(new_lst)

5)
words = []  
n = int(input("Enter the range of the list: "))

for i in range(n):
    words.append(input("Enter the elements of the string: "))


filtered_words = list(filter(lambda char: len(char) <= 8, words))

print(filtered_words)




































