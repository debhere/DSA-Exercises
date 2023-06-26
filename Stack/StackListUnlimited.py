class StackListUnlimited:
    def __init__(self):
        self.stack = []

    def __str__(self):
        valueStr = reversed(self.stack)
        valueStr = [str(element) for element in valueStr]
        return '\n'.join(valueStr)

    def isEmpty(self):
        isVoid = True
        if self.stack:
            isVoid = False
        return isVoid

    def push(self, element):
        self.stack.append(element)
        return "{} is Pushed into the stack".format(element)

    def pop(self):
        isPopped = False
        if self.stack:
            self.stack.pop()
            isPopped = True
        return isPopped

    def peek(self):
        ele = None
        if self.stack:
            ele = self.stack[len(self.stack) - 1]
        return ele

    def delete(self):
        isDeleted = False
        if self.stack:
            self.stack = None
            isDeleted = True
        return isDeleted

    def getLength(self):
        return len(self.stack)


stackList = StackListUnlimited()

print(stackList.isEmpty())
print(stackList.push(3))
print(stackList.push(2))
print(stackList.push(1))
print(stackList.push(0))
print(stackList.getLength())
print(stackList)
print(stackList.pop())
print(stackList.isEmpty())
print(stackList)
print(stackList.peek())
stackList.delete()
print(stackList.isEmpty())
