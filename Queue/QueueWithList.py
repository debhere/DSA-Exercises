class QueueWithList:
    def __init__(self):
        self.items = []

    def __str__(self):
        queue = [str(item) for item in self.items]
        return '\n'.join(queue)

    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def enqueue(self, item):
        self.items.append(item)
        return

    def dequeue(self):
        return False if self.isEmpty() else self.items.pop(0)

    def peek(self):
        return self.items[0]

    def deleteQueue(self):
        self.items = None


q = QueueWithList()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
print()
q.dequeue()
print(q)
print(q.peek())


