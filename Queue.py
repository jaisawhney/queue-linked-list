from LinkedList import LinkedList


class Queue:

    def __init__(self):
        # dynamic array
        # [1, 3, 3, 4]          ]
        # front   back
        self.items = LinkedList()

    def size(self):
        return self.items.length()

    def is_empty(self):
        return self.size() > 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)


my_queue = Queue()

my_queue.enqueue(100)
my_queue.enqueue(5)
my_queue.enqueue(20)

print(my_queue.items)

my_queue.dequeue()
my_queue.dequeue()

print(my_queue.items)
