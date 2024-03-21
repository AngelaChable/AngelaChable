from abc import ABC, abstractmethod
class QueueInterface(ABC):

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def front(self):
        pass

    @abstractmethod
    def enqueue(self, info):
        pass

    @abstractmethod
    def dequeue(self):
        pass

class Queue(QueueInterface):
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def enqueue(self, info):
        self.items.append(info)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def dump(self):
        print("********* QUEUE DUMP *********")
        print("   Size:", self.size())
        for i, item in enumerate(self.items, 1):
            print("   ** Element", i)
            print("     Customer:", item.get_customer())
            print("     Quantity:", item.get_qtty())
            print("     ------------")
        print("******************************")

class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty
        self.next = None  

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


queue = Queue()
queue.enqueue(Order(20, "cust1"))
queue.enqueue(Order(30, "cust2"))
queue.enqueue(Order(40, "cust3"))
queue.enqueue(Order(50, "cust3"))

queue.dump()

node = queue.front()
while node is not None:
    print("Customer:", node.get_customer())
    print("Quantity:", node.get_qtty())
    node = node.next  
