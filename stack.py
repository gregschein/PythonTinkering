class Stack(object):
    def __init__(self, initialState):
        self.internalStack = initialState
    def push(self, number):
        self.internalStack.append(number)
        return self
    def pop(self):
        return self.internalStack.pop()
    def getStack(self):
        return self.internalStack