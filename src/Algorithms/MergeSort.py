__author__ = 'ingthor'
from src.Algorithms import Utils


def Merge(lArray, rArray):
    outPutArray = []
    i = 0
    j = 0
    while i < len(lArray) and j < len(rArray):  # comparea við iteratorana
        if lArray[i] <= rArray[j]:
            outPutArray.append(lArray[i])
            i += 1
        else:
            outPutArray.append(rArray[j])
            j += 1

    # hvað gerir þetta?Ð
    if lArray:
        outPutArray.extend(lArray[i:])
    if rArray:
        outPutArray.extend(rArray[j:])

    return outPutArray


def MergeSort(A):
    if (len(A) <= 1):
        return A
    left = MergeSort(A[:(len(A) // 2)])
    right = MergeSort(A[(len(A) // 2):])
    return list(Merge(left, right))


def Test(n):
    testA = Utils.RandomArray(n)
    print(testA)
    testA = MergeSort(testA)
    print(testA)
    return
