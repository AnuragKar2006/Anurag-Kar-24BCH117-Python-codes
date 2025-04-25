1)
import random

odd_integers = [random.choice(range(1, 100, 2))
 for _ in range(5):
  print("List of 5 odd integers:", odd_integers)
even_integers = [random.choice(range(0, 100, 2))
 for _ in range(4):
  print("List of 4 even integers:", even_integers)
 if odd_integers[2] = even_integers:
  print("Updated odd integers list:", odd_integers)
flattened_list = [item for sublist in odd_integers for item in (sublist if
isinstance(sublist, list) else [sublist])]
print("Flattened list:", flattened_list)
sorted_list = sorted(flattened_list)
print("Sorted list:", sorted_list)

2)
import random

random_integers = [random.randint(1, 100) for _ in range(20)]
print("List of 20 random integers:", random_integers)
target_number = int(input("Enter a number to find its positions: "))
positions = [index for index, value in enumerate(random_integers)
if value == target_number:
print("Positions of occurrences:", positions)

3)
import random

random_integers = [random.randint(1, 100)
for _ in range(20):
print("List of 20 random integers:", random_integers)
target_number = int(input("Enter a number to find its positions: "))
positions = [index for index, value in enumerate(random_integers)
if value == target_number:
print("Positions of occurrences:", positions)

4)
import random

random_numbers = [random.randint(1, 30)
for _ in range(50):
print("List of 50 random numbers:", random_numbers)
unique_numbers = list(set(random_numbers))
print("List after removing duplicates:", unique_numbers)

5)
strings_list = ["apple", "banana", "cherry", "date", "elderberry"]

print("Original list of strings:", strings_list)
uppercase_list = [string.upper() for string in strings_list]
print("List in uppercase:", uppercase_list)

6)
fahrenheit_temps = [32, 68, 77, 104, 122]

print("Temperatures in Fahrenheit:", fahrenheit_temps)
celsius_temps = [(temp - 32) * 5 / 9 for temp in fahrenheit_temps]
print("Equivalent temperatures in Celsius:", celsius_temps)


7)
class Stack:

def __init__(self):
self.stack = []
def push(self, item):
self.stack.append(item)
def pop(self):
if not self.is_empty():
return self.stack.pop()
return None
def is_empty(self):
return len(self.stack) == 0
def display(self):
print("Stack elements:", self.stack)
stack = Stack()
while True:
print("\nStack Operations:")
print("1. Push")
print("2. Pop")
print("3. Display")
print("4. Exit") c
hoice = int(input("Enter your choice: "))

if choice == 1:
item = int(input("Enter the item to push: "))
stack.push(item)
print(f"{item} pushed onto stack.")
elif choice == 2:
item = stack.pop()
if item:
print(f"Popped item: {item}")
else:
print("Stack is empty.")
elif choice == 3:
stack.display()
elif choice == 4:
break else:
print("Invalid choice! Please try again.")

8)
class Queue:
def __init__(self):
self.queue = []
def enqueue(self, item):
self.queue.append(item)
def dequeue(self):
if not self.is_empty():
return self.queue.pop(0)
return None
def is_empty(self):
return len(self.queue) == 0
def display(self):
print("Queue elements:", self.queue)
queue = Queue()
while True:
print("\nQueue Operations:")
print("1. Enqueue")
print("2. Dequeue")
print("3. Display")
print("4. Exit")
choice = int(input("Enter your choice: "))

if choice == 1:
item = int(input("Enter the item to enqueue: "))
queue.enqueue(item)
print(f"{item} enqueued to queue.")
elif choice == 2:
item = queue.dequeue()
if item:
print(f"Dequeued item: {item}")
else: print("Queue is empty.")
elif choice == 3:
queue.display()
elif choice == 4:
break else:
print("Invalid choice! Please try again.")

9)
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3 = [num for num in list1 if num not in list2]
print("Numbers in list1 but not in list2:", list3)





































