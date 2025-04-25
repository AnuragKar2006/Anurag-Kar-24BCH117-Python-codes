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
