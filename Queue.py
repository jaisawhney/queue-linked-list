from LinkedList import LinkedList


class Queue:

    def __init__(self):
        self.items = LinkedList()

    def size(self):
        return self.items.length()

    def is_empty(self):
        return self.items.is_empty()

    def enqueue(self, item):
        # add to the rear/tail
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        # remove from the front/head
        front = self.items.head
        self.items.delete(front.data)
        return front


my_queue = Queue()

my_queue.enqueue(1)
print(my_queue.items)  # [(1)]

my_queue.enqueue(2)
print(my_queue.items)  # [(1) -> (2)]

my_queue.enqueue(3)
print(my_queue.items)  # [(1) -> (2) -> (3)]

my_queue.dequeue()
my_queue.dequeue()

print(my_queue.items)  # [(3)]
