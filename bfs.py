from Node import *
import numpy as numpy

fringe = []
closed_list = []

goalNode = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

rootNode = numpy.array([[1, 2, 3, 0], [5, 6, 7, 4], [9, 10, 11, 8], [13, 14, 15, 12]])

def bfs_search(data):
    root_node = Node(data, None)
    fringe.append(root_node)
    closed_list.append(data.tolist())

    while fringe:
        currentNode = fringe.pop(0)

        if (currentNode.data.tolist() == goalNode.tolist()):
            receive_goal(currentNode)
            return

        move1 = moveUp(currentNode.data)
        if move1 is not None:
            next_data = move1
            if next_data.tolist() not in closed_list:
                new_node = Node(next_data, currentNode)
                closed_list.append(next_data.tolist())
                fringe.append(new_node)

        move2 = moveDown(currentNode.data)
        if move2 is not None:
            next_data = move2
            if next_data.tolist() not in closed_list:
                new_node = Node(next_data, currentNode)
                closed_list.append(next_data.tolist())
                fringe.append(new_node)

        move3 = moveLeft(currentNode.data)
        if move3 is not None:
            next_data = move3
            if next_data.tolist() not in closed_list:
                new_node = Node(next_data, currentNode)
                closed_list.append(next_data.tolist())
                fringe.append(new_node)

        move4 = moveRight(currentNode.data)
        if move4 is not None:
            next_data = move4
            if next_data.tolist() not in closed_list:
                new_node = Node(next_data, currentNode)
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

bfs_search(rootNode)


