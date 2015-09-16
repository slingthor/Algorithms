__author__ = 'ingthor'
import random

class Stack(object):
    stackList = []
    count = 0

    def __init__(self):
        self.stackList = []
        self.count = 0

    def Push(self, elem):
        self.stackList.append(elem)
        self.count += 1

    def Pop(self):
        if self.Empty():
            raise Exception

        temp = self.stackList[self.count-1]
        self.Delete()
        return temp

    def Delete(self):
        self.stackList.remove(self.count-1)
        self.count -= 1
        return

    def Empty(self):
        if self.count is 0:
            return True
        else:
            return False


def Test(n):
    testStack = Stack()
    for i in range(0,n):
        temp = random.randint(0,n)
        print(temp, end=' ')
        testStack.Push(temp)
    print()
    for i in range(0,n):
        print(testStack.Pop(), end=' ')


