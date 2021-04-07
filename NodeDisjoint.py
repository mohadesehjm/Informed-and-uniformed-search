import numpy as numpy
class Node :
    def __init__(self,data,parent,cost):
        self.data = data
        self.parent = parent
        self.cost = cost


    def getCost(self):
        return (self.cost)


def moveUp(data):
    notValue = True
    arr = numpy.copy(data)
    for i in range(4) :
        for j in range(4) :
            if arr[i][j] == 0 :
                zero_i = i
                zero_j = j
                break
    if zero_i > 0 :
        if arr[zero_i - 1][zero_j] == -1:
            notValue = False
        arr[zero_i][zero_j] = arr[zero_i -1][zero_j]
        arr[zero_i-1][zero_j] = 0
        return [arr,notValue]
    return [None]

def moveDown(data):
    notValue = True
    arr = numpy.copy(data)
    for i in range(4) :
        for j in range(4) :
            if arr[i][j] == 0 :
                zero_i = i
                zero_j = j
    if zero_i < 3 :
        if arr[zero_i + 1][zero_j] == -1:
            notValue = False
        arr[zero_i][zero_j] = arr[zero_i + 1][zero_j]
        arr[zero_i +1][zero_j] = 0
        arr
        return [arr,notValue]
    return [None]

def moveRight(data):
    notValue = True
    arr = numpy.copy(data)
    for i in range(4) :
        for j in range(4) :
            if arr[i][j] == 0 :
                zero_i = i
                zero_j = j
    if zero_j < 3 :
        if arr[zero_i][zero_j + 1] == -1:
            notValue = False
        arr[zero_i][zero_j] = arr[zero_i][zero_j +1]
        arr[zero_i][zero_j + 1] = 0
        return [arr,notValue]
    return [None]

def moveLeft(data):
    notValue = True
    arr = numpy.copy(data)
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                zero_i = i
                zero_j = j
    if zero_j > 0 :
        if arr[zero_i][zero_j - 1] == -1:
            notValue = False
        arr[zero_i][zero_j] = arr[zero_i][zero_j - 1]
        arr[zero_i][zero_j - 1 ] = 0
        return [arr,notValue]
    return [None]