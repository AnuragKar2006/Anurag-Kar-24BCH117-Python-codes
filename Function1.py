1)
str = ''
def upp_low(str):
    str = input("Enter a string")
    a=b=c=0
    for i in str:
        if i.isupper()==True:
            a+=1
        
        else:
            c+=1
    dict ={"Uppercase" : a , "Lowercase":c}
    print(dict)
upp_low(str)

2)
def compute(n):
   
    n1 = int(str(n))
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    n4 = int(str(n) * 4)
    
    return n1 + n2 + n3 + n4


for i in range(4, 8):
    print(f"compute({i}) = {compute(i)}")



3)
def create_array(x, y, z, value):
   
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]


array = create_array(3, 4, 5, 7)
for layer in array:
    for row in layer:
        print(row)
    print()

4)
avg=0
sum=0
def sum_avg(avg,sum):
    sub1=int(input("Enter the marks of first subject"))
    sub2=int(input("Enter the marks of second subject"))
    sub3=int(input("Enter the marks of third subject"))
    sub4=int(input("Enter the marks of fourth subject"))
    sub5=int(input("Enter the marks of fifth subject"))
    sum = sub1+sub2+sub3+sub4+sub5
    avg=sum/5
    return avg,sum
print(sum_avg(avg,sum))

5)
import string

def ispangram(sentence):
    
    sentence_set = set(sentence.lower())
    
   
    alphabet_set = set(string.ascii_lowercase)
    
    
    return alphabet_set <= sentence_set

test_sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Crazy Fredrick bought many very exquisite opal jewels",
    "Hello world!"
]

for sentence in test_sentences:
    print(f"'{sentence}' is a pangram: {ispangram(sentence)}")


6)
def generate_tuples(n):
    return [(x, x**2, x**3) for x in range(1, n + 1)]


end_value = int(input("Enter the ending value: "))
result = generate_tuples(end_value)
print(result)


7)
str=""
def ispalindrome(str):
    str =input("Enter a string")
    rev_str=str[::-1]
    if(str==rev_str):
        print("The string is palindrome")
    else:
        print("The string is not palindrome")
ispalindrome(str)

8)
def convert(str1):
    str1=input("Enter a string: ")
    str1=str1.strip()
    print(str1)


user_input = ""
convert(user_input) 


10)
def frequency(str1):
    str1 = str1.upper() 
    char_dict = {}  

    c, d = 0, 0  

    for char in str1:
        if 'A' <= char <= 'Z':  
            c += 1
        else:
            d += 1
        
     
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

  
    sorted_dict = dict(sorted(char_dict.items()))

    print("Character Frequencies:", sorted_dict)
    print("Letter Count:", c)
    print("Non-Letter Count:", d)


str = input("Enter a string: ")
frequency(str)

11)
list1 =[]
list2=[]
list3=[]
def create_list(l1,l2,l3):
    l1=[]
    l2=[]
    
    n = int(input("Enter the range of the list"))
    for i in range(1,n+1):
        l1.append(int(input("Enter the values of list one")))
    for j in range(1,n+1):
        l2.append(int(input("Enter the values of list two")))
    s1=set(l1)
    s2=set(l2)
    l3=[s1.intersection(s2)]
    
    print(l3)
   
create_list(list1,list2,list3)




































    