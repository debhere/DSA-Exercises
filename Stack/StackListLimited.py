class StackListLimited:
    def __init__(self, maxsize=6):
        self.stack = []
        self.maxSize = maxsize

    def __str__(self):
        values = reversed(self.stack)
        values = [str(value) for value in values]
        return '\n'.join(values)

    def isEmpty(self):
        isVoid = True
        if self.stack:
            isVoid = False
        return isVoid

    def isFull(self):
        isFilled = True
        if len(self.stack) < self.maxSize:
            isFilled = False
        return isFilled

    def push(self, element):
        message = 'None'
        if not self.isFull():
            self.stack.append(element)
            message = '{} is pushed'.format(element)
        return message

    def pop(self):
        isPopped = False
        if not self.isEmpty():
            self.stack.pop()
            isPopped = True
        return isPopped

    def peek(self):
        ele = None
        if not self.isEmpty():
            ele = self.stack[len(self.stack) - 1]
        return ele

    def getLength(self):
        return len(self.stack)


stackList = StackListLimited(maxsize=4)

print(stackList.isEmpty())
print(stackList.push(3))
print(stackList.push(2))
print(stackList.push(1))
print(stackList.push(0))
print(stackList.push(-1))
print(stackList.isFull())



