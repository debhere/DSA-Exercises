class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        val = [str(x.value) for x in self.linkedList]
        return ' '.join(val)

    def enqueue(self, value):
        newNode = Node(value)
        if not self.linkedList.head:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            temp = self.linkedList.tail
            self.linkedList.tail = newNode
            temp.next = self.linkedList.tail

    def dequeue(self):
        if not self.linkedList.head:
            return None
        else:
            temp = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return temp

    def isEmpty(self):
        flag = True
        if self.linkedList.head:
            flag = False
        return flag


q = Queue()
q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print()
q.dequeue()
print(q)
