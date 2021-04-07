import numpy as numpy
from Node import *
fringe = [] #queue
fringe2 = []
close_List = []
close_list2 = []

goalNode = numpy.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15,0]]).reshape(4,4)

rootNode = numpy.array([[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 15, 11],
             [0, 13, 14, 12]]).reshape(4,4)


def Search_in_closeList(newNode):
    for index in close_List:
        if newNode is index:
            return False
    return True

def Search_in_closeList2(newNode):
    for index in close_list2:
        if newNode is index:
            return False
    return True

def bds_search(data):
    root_node = Node(data, None)
    goal_node = Node(goalNode,None)
    fringe.append(root_node)
    fringe2.append((goal_node))
    close_List.append(data)
    close_list2.append(goalNode)
    while True :
        CurrentNode = fringe.pop(0)
        for index in fringe2 :
            if(CurrentNode.data.tolist() == index.data.tolist()) :  #با تک تک گره های داخل فرینح بایذ  مقایسه شود
                receive_goal(CurrentNode,index)
                return 0
        forward(CurrentNode)
        CurrentNode2 = fringe2.pop(0)
        for index in fringe:
            if (CurrentNode2.data.tolist() == index.data.tolist()):  # با تک تک گره های داخل فرینح بایذ  مقایسه شود
                receive_goal(index, CurrentNode2)
                return 0
        backward(CurrentNode2)

def forward(CurrentNode) :
        move = moveUp(CurrentNode.data)
        if move is not None:
            next_data = move
            if Search_in_closeList(next_data) :
                new_node = Node(next_data, CurrentNode)
                close_List.append(next_data)
                fringe.append(new_node)
        move = moveDown(CurrentNode.data)
        if move is not None:
            next_data = move
            if Search_in_closeList(next_data):
                new_node = Node(next_data, CurrentNode)
                close_List.append(next_data)
                fringe.append(new_node)
        move = moveLeft(CurrentNode.data)
        if move is not None:
            next_data = move
            if Search_in_closeList(next_data):
                new_node = Node(next_data, CurrentNode)
                close_List.append(next_data)
                fringe.append(new_node)
        move = moveRight(CurrentNode.data)
        if move is not None:
            next_data = move
            if Search_in_closeList(next_data):
                new_node = Node(next_data, CurrentNode)
                close_List.append(next_data)
                fringe.append(new_node)
def backward(CurrentNode) :
        move = moveUp(CurrentNode.data)
        if move is not None:
            next_data = move
            if Search_in_closeList2(next_data) :
                new_node = Node(next_data, CurrentNode)
                close_list2.append(next_data)
                fringe2.append(new_node)
        move = moveDown(CurrentNode.data)
        if move is not None:
            next_data = move
            if Search_in_closeList2(next_data):
                new_node = Node(next_data, CurrentNode)
                close_list2.append(next_data)
                fringe2.append(new_node)
        move = moveLeft(CurrentNode.data)
        if move is not None:
            next_data = move
            if Search_in_closeList2(next_data):
                new_node = Node(next_data, CurrentNode)
                close_list2.append(next_data)
                fringe2.append(new_node)
        move = moveRight(CurrentNode.data)
        if move is not None:
            next_data = move
            if Search_in_closeList2(next_data):
                new_node = Node(next_data, CurrentNode)
                close_list2.append(next_data)
                fringe2.append(new_node)

def receive_goal(CurrentNode,goal_node):
    arr_path = []
    arr_path.append(CurrentNode.data)
    temp = CurrentNode.parent
    while  temp != None :
        arr_path.append(temp.data)
        temp = temp.parent
    arr_path2 = []
    arr_path2.append(goal_node.data)
    temp = goal_node.parent
    while temp != None:
        arr_path2.append(temp.data)
        temp = temp.parent

    arr_path.reverse()

    for i in arr_path:
        print(i)
        print(" ")


    for i in range(len(arr_path2)-1):
        print(arr_path2[i+1])
        print(" ")
    return 0 ;


import time

start = time.time()

bds_search(rootNode)


end = time.time()
print(end - start)