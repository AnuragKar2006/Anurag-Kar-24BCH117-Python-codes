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