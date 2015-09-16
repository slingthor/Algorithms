__author__ = 'ingthor'
from Algorithms import Utils
import random

class LinkedList(object):
    __head = None



    def Insert(self, elem):
        if self.__head is None:
            self.__head = Node(elem, None, Node(None, self.__head, None))
        else:
            insertNode = Node(elem, None, self.__head)
            self.__head.prev = insertNode
            self.__head = insertNode

    def DeleteNode(self, node):
        if node.prev is not None:
            self.node.prev.next = node.next
        else:
            self.__head = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def Search(self, elem):
        pointer = self.__head
        while(pointer.elem is not elem and pointer.next is not None):
            pointer = pointer.next
        return pointer.elem

    def TestCheat(self):
        return self.__head

    #Bad idea, most likely remove
    '''
    def Append(self, elem):
        if self.__head is None:
            __head = Node(elem, None, None)
        else:
            self.Add(elem, self.__head.next)

    def __Append(self, elem, node):
        if node.next is not None:
            self.__Add(self, elem, node.next)
        else:
            node.next = Node(elem,node,None)
    '''

class Node(object):

    def __init__(self, key,prev,next):
        self.key = key
        self.prev = prev
        self.next = next

    key = None
    prev = None
    next = None

def Test(n):
    testLinkedList = LinkedList()
    testA = Utils.RandomArray(n)
    for elem in testA:
        rand = random.randint(0,n)
        testLinkedList.Insert(rand)
        print(rand, end=' ')
    print()
    pointer = testLinkedList.TestCheat()
    for i in range(0,n):
        print(pointer.key, end=' ')
        pointer = pointer.next
    return