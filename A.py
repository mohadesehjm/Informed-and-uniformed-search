from NodeA import *
from manhatan import *
import numpy as numpy

fringe = []
closed_list = []

goalNode = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]).reshape(4, 4)

rootNode = numpy.array([[1, 2, 3, 0], [5, 6, 7, 4], [9, 10, 11, 8], [13, 14, 15, 12]]).reshape(4, 4)


def Search_in_closedList(newNode):
    for index in closed_list:
        if newNode is index:
            return False
    return True


def A_star(data):
    root_node = NodeA(data, None,0 ,0)
    manhatan = manhattan_distance(root_node)
    root_node.hn = manhatan
    fringe.append(root_node)
    closed_list.append(data.tolist())
    while fringe:
        currentNode = min(fringe, key=getFn)
        fringe.remove(currentNode)
        if (currentNode.data.tolist() == goalNode.tolist()):
            receive_goal(currentNode)
            return 0

        move1 = moveUp(currentNode.data)
        if move1 is not None:
            next_data = move1
            if next_data.tolist() not in closed_list:
                new_node = NodeA(next_data, currentNode, currentNode.gn + 7, 0)
                manhatan = manhattan_distance(new_node)
                new_node.hn = manhatan
                closed_list.append(next_data.tolist())
                fringe.append(new_node)

        move2 = moveDown(currentNode.data)
        if move2 is not None:
            next_data = move2
            if next_data.tolist() not in closed_list:
                new_node = NodeA(next_data, currentNode, currentNode.gn + 1, 0)
                manhatan = manhattan_distance(new_node)
                new_node.hn = manhatan
                closed_list.append(next_data.tolist())
                fringe.append(new_node)

        move3 = moveLeft(currentNode.data)
        if move3 is not None:
            next_data = move3
            if next_data.tolist() not in closed_list:
                new_node = NodeA(next_data, currentNode, currentNode.gn + 5, 0)
                manhatan = manhattan_distance(new_node)
                new_node.hn = manhatan
                closed_list.append(next_data.tolist())
                fringe.append(new_node)

        move4 = moveRight(currentNode.data)
        if move4 is not None:
            next_data = move4
            if next_data.tolist() not in closed_list:
                new_node = NodeA(next_data, currentNode, currentNode.gn + 6, 0)
                manhatan = manhattan_distance(new_node)
                new_node.hn = manhatan
                closed_list.append(next_data.tolist())
                fringe.append(new_node)

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

A_star(rootNode)
# print("close " ,closed_list )
