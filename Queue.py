from LinkedList import LinkedList


class Queue:

    def __init__(self):
        self.items = LinkedList()

    def size(self):
        return self.items.length()

    def is_empty(self):
        return self.items.is_empty()

    def enqueue(self, item):
        # add to the rear/head
        self.items.prepend(item)

    def dequeue(self):
        if self.is_empty():
            return None

        # remove from the front/tail
        front = self.items.tail
        self.items.delete(front.data)
        return front


my_queue = Queue()

my_queue.enqueue(100)
print(my_queue.items)  # [(100)]

my_queue.enqueue(5)
print(my_queue.items)  # [(5) -> (100)]

my_queue.enqueue(20)
print(my_queue.items)  # [(20) -> (5) -> (100)]

my_queue.dequeue()
my_queue.dequeue()

print(my_queue.items)  # [(20)]
