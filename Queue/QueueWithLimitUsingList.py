class QueueWithLimit:
    def __init__(self, limit=4):
        self.items = []
        self.limit = limit

    def __str__(self):
        que = [str(item) for item in self.items]
        return '\n'.join(que)

    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def isFull(self):
        return True if len(self.items) == self.limit else False

    def enqueue(self, item):
        isInserted = False
        if not self.isFull():
            self.items.append(item)
            isInserted = True
        return isInserted

    def dequeue(self):
        return False if self.isEmpty() else self.items.pop(0)

    def peek(self):
        return None if self.isEmpty() else self.items[0]


q = QueueWithLimit()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.isFull())
