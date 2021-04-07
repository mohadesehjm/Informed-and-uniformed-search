from NodeDisjoint import *
import numpy as numpy
import pickle
fringe = []
closed_list = []

goalNode = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

rootNode1 = numpy.array([[1, 2, -1, -1], [5, -1, -1, -1], [9, -1, -1, -1], [13, -1, -1, 0]])
rootNode2 = numpy.array([[-1, -1, 3, 4], [-1, 6, -1, -1], [-1, 10, -1, -1], [-1, 14, -1, 0]])
rootNode3 = numpy.array([[-1, -1, -1, -1], [-1, -1, 7, 8], [-1, -1, 11, 12], [-1, -1, 15, 0]])


arr1 = numpy.array([1, 2, 5, 9, 13])
arr2 = numpy.array([3, 4, 6, 10, 14])
arr3 = numpy.array([7, 8, 11, 12, 15])

def convet_to_string(data,arr):
    result = ""
    for i in range(5):
        index_i = numpy.where(data == arr[i])[0][0]
        index_j = numpy.where(data == arr[i])[1][0]
        result += str(index_i)
        result += str(index_j)

    return result


def disjoint_database(data):
    root_node = Node(data, None,0)
    fringe.append(root_node)
    closed_list.append(data.tolist())
    if(data.tolist() == rootNode1.tolist()) :
        filename = "dataBase.p"
        arr = numpy.copy(arr1)
    elif data.tolist() == rootNode2.tolist() :
        filename = "dataBase1.p"
        arr = numpy.copy(arr2)
    elif data.tolist() == rootNode3.tolist() :
        filename = "dataBase2.p"
        arr = numpy.copy(arr3)
    else :
        print("data is not correct")
        return 0
    dic = {convet_to_string(root_node.data,arr) : 0}
    pickle.dump(dic ,open(filename, "wb"))
    while fringe:
        currentNode = fringe.pop(0)
        dic = pickle.load(open(filename, "rb"))
        move = moveUp(currentNode.data)
        move1 = move[0]
        if move1 is not None:
            next_data = move1
            if next_data.tolist() not in closed_list:
                if (move[1]) :
                    dic.update({convet_to_string(move1,arr) : currentNode.getCost() + 1})
                    new_node = Node(next_data, currentNode, currentNode.getCost()+1)
                else :
                    new_node = Node(next_data, currentNode, currentNode.getCost())
                closed_list.append(next_data.tolist())
                fringe.append(new_node)
                pickle.dump(dic, open(filename, "wb"))

        move = moveDown(currentNode.data)
        move2 = move[0]
        if move2 is not None:
            next_data = move2
            if next_data.tolist() not in closed_list:
                if (move[1]) :
                    dic.update({convet_to_string(move2,arr) : currentNode.getCost() + 1})
                    new_node = Node(next_data, currentNode, currentNode.getCost()+1)
                else :
                    new_node = Node(next_data, currentNode, currentNode.getCost())
                closed_list.append(next_data.tolist())
                fringe.append(new_node)
                pickle.dump(dic, open(filename, "wb"))

        move = moveLeft(currentNode.data)
        move3 = move[0]
        if move3 is not None:
            next_data = move3
            if next_data.tolist() not in closed_list:
                if (move[1]):
                    dic.update({convet_to_string(move3, arr): currentNode.getCost() + 1})
                    new_node = Node(next_data, currentNode, currentNode.getCost() + 1)
                else:
                    new_node = Node(next_data, currentNode, currentNode.getCost())
                closed_list.append(next_data.tolist())
                fringe.append(new_node)
                pickle.dump(dic, open(filename, "wb"))

        move = moveRight(currentNode.data)
        move4 = move[0]
        if move4 is not None:
            next_data = move4
            if next_data.tolist() not in closed_list:
                if (move[1]):
                    dic.update({convet_to_string(move4, arr): currentNode.getCost() + 1})
                    new_node = Node(next_data, currentNode, currentNode.getCost() + 1)
                else:
                    new_node = Node(next_data, currentNode, currentNode.getCost())
                closed_list.append(next_data.tolist())
                fringe.append(new_node)
                pickle.dump(dic, open(filename, "wb"))
        pickle.dump(dic, open(filename, "wb"))


import time

# disjoint_database(rootNode3)

# filename = 'dataBase1.p'
# infile = open(filename,'rb')
# new_dict = pickle.load(infile)
# infile.close()
# # if {'0001102030': 0 }in new_dict :
# # print(new_dict["0001102031"])
# print(new_dict["0313112131"])
# print(type(new_dict))


res = numpy.where(goalNode == 16)
stri = " "
stri = stri +str(res)
# print(convet_to_string(rootNode1,arr))
