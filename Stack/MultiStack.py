class MultiStack:
    def __init__(self, stack_size=3, num_stack=3):
        self.num_stack = num_stack
        self.stack_size = stack_size
        self.array = [0] * (self.num_stack * self.stack_size)
        self.stack = [0] * self.stack_size

    def isEmpty(self):
        if sum(self.array) == 0:
            return True
        else:
            return False

    def push(self, element):
        # if self.isEmpty():
        #     self.stack.append(element)
        # elif len(sta)
        pass

    def pop(self):
        pass

