__author__ = 'ingthor'
#TODO finish heapsort
from src.Algorithms import Utils

class MaxHeap(object):
    heapArray = []
    heapSize = 0

    def __init__(self, initArray):
        self.heapArray = initArray
        self.__BuildMaxHeap()
        print(self.heapArray)
        # finish implementation

    def __MaxHeapify(self, i):
        left = self.__Left(i)
        right = self.__Right(i)
        if(i is 0):
            left = 1
            right = 2

        largest = 0
        if left < len(self.heapArray) and self.heapArray[left] > self.heapArray[i]:
            largest = left
        else:
            largest = i

        if right < len(self.heapArray) and self.heapArray[right] > self.heapArray[largest]:
            largest = right

        if largest != i:
            self.heapArray[i], self.heapArray[largest] = self.heapArray[largest], self.heapArray[i]
            self.__MaxHeapify(largest)
        return

    def __BuildMaxHeap(self):
        self.heapSize = len(self.heapArray)
        for i in range(len(self.heapArray)//2, 0, -1):

            self.__MaxHeapify(i)
        return

    def Heapsort(self):
        self.__BuildMaxHeap()
        print(len(self.heapArray))
        for i in range(len(self.heapArray)-1, 1,-1):
            self.heapArray[0], self.heapArray[i] = self.heapArray[i], self.heapArray[0]
            self.__MaxHeapify(0)
        return self.heapArray

    def Insert(self):
        return

    def Extract(self):
        return

    def Increase(self):
        return

    def Max(self):
        return


    def __Parent(self, i):
        #return i >> 1  # i/2
        return i//2

    def __Left(self, i):
        #return i << 1  # 2i
        return i*2

    def __Right(self, i):
        #return i << 1 + 1  # 2i+1
        return i*2+1

def Test(n):
    testA = Utils.RandomArray(n)
    print(testA)
    testHeap = MaxHeap(testA)
    testA = testHeap.Heapsort()
    print(testA)
    return