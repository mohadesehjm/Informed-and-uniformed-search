from NodeA import *
from manhatan import *
import numpy as numpy
from disgoint import convet_to_string
import pickle
fringe = []
closed_list = []

goalNode = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]).reshape(4, 4)

rootNode = numpy.array([[1, 2, 3, 0], [5, 6, 7, 4], [9, 10, 11, 8], [13, 14, 15, 12]]).reshape(4, 4)
arr1 = numpy.array([1, 2, 5, 9, 13])
arr2 = numpy.array([3, 4, 6, 10, 14])
arr3 = numpy.array([7, 8, 11, 12, 15])
def getHeuristic(data):
    res1 = res2 = res3 = 0
    filename = 'dataBase.p'
    infile = open(filename, 'rb')
    new_dict = pickle.load(infile)
    infile.close()
    inde1 = convet_to_string(data,arr1)
    if type(inde1) is str :
        res1 = new_dict[inde1]

    filename = 'dataBase1.p'
    infile = open(filename, 'rb')
    new_dict = pickle.load(infile)
    infile.close()
    inde2 = convet_to_string(data, arr2)
    if type(inde2) is str :
        res2 = new_dict[inde2]

    filename = 'dataBase2.p'
    infile = open(filename, 'rb')
    new_dict = pickle.load(infile)
    infile.close()
    inde3 = convet_to_string(data, arr3)
    if type(inde3) is str :
        res3 = new_dict[inde3]

    result = res1 + res2 + res3
    return result


def IDA_star(data):
    root_node = NodeA(data, None,0 ,getHeuristic(data))
    cutOff = getHeuristic(data)
    achieve = False

    while not achieve:
        fringe.append(root_node)
        closed_list.append(data.tolist())
        while fringe :
            currentNode = fringe.pop(len(fringe)-1)
            if(getFn(currentNode) > cutOff):
                continue
            if (currentNode.data.tolist() == goalNode.tolist()):
                receive_goal(currentNode)
                achieve = True
                break

            move1 = moveUp(currentNode.data)
            if move1 is not None:
                next_data = move1
                if next_data.tolist() not in closed_list:
                    new_node = NodeA(next_data, currentNode, currentNode.gn + 5, getHeuristic(next_data))
                    closed_list.append(next_data.tolist())
                    fringe.append(new_node)

            move2 = moveDown(currentNode.data)
            if move2 is not None:
                next_data = move2
                if next_data.tolist() not in closed_list:
                    new_node = NodeA(next_data, currentNode, currentNode.gn + 1, getHeuristic(next_data))
                    closed_list.append(next_data.tolist())
                    fringe.append(new_node)

            move3 = moveLeft(currentNode.data)
            if move3 is not None:
                next_data = move3
                if next_data.tolist() not in closed_list:
                    new_node = NodeA(next_data, currentNode, currentNode.gn + 4, getHeuristic(next_data))
                    closed_list.append(next_data.tolist())
                    fringe.append(new_node)

            move4 = moveRight(currentNode.data)
            if move4 is not None:
                next_data = move4
                if next_data.tolist() not in closed_list:
                    new_node = NodeA(next_data, currentNode, currentNode.gn + 6, getHeuristic())
                    closed_list.append(next_data.tolist())
                    fringe.append(new_node)

            Min = manhattan_distance(min(fringe, key = manhattan_distance))

        if not achieve :
            cutOff = Min

def receive_goal(currentNode):
    arr_path = []
    arr_path.append(currentNode.data)
    temp = currentNode.parent
    while temp != None:
        arr_path.append(temp.data)
        temp = temp.parent

    arr_path.reverse()
    for index in arr_path:
        print(index.tolist())


import time

IDA_star(rootNode)
