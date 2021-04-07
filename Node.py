import numpy as numpy
class Node :
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent

def moveUp(data):
    arr = numpy.copy(data)
    for i in range(4) :
        for j in range(4) :
            if arr[i][j] == 0 :
                zero_i = i
                zero_j = j
                break
    if zero_i > 0 :
        arr[zero_i][zero_j] = arr[zero_i -1][zero_j]
        arr[zero_i-1][zero_j] = 0
        return arr
    return None

def moveDown(data):
    arr = numpy.copy(data)
    for i in range(4) :
        for j in range(4) :
            if arr[i][j] == 0 :
                zero_i = i
                zero_j = j
    if zero_i < 3 :
        arr[zero_i][zero_j] = arr[zero_i + 1][zero_j]
        arr[zero_i +1][zero_j] = 0
        arr
        return arr
    return None

def moveRight(data):
    arr = numpy.copy(data)
    for i in range(4) :
        for j in range(4) :
            if arr[i][j] == 0 :
                zero_i = i
                zero_j = j
    if zero_j < 3 :
        arr[zero_i][zero_j] = arr[zero_i][zero_j +1]
        arr[zero_i][zero_j + 1] = 0
        return arr
    return None

def moveLeft(data):
    arr = numpy.copy(data)
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                zero_i = i
                zero_j = j
    if zero_j > 0 :
        arr[zero_i][zero_j] = arr[zero_i][zero_j - 1]
        arr[zero_i][zero_j - 1 ] = 0
        return arr
    return None