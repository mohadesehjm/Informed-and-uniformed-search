from NodeA import *
goalNode = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15,0]]

rootNode = [[1, 2, 3, 0], [5, 6, 7, 4], [9, 10, 11, 8], [13, 14, 15, 12]]
def manhattan_distance(data):
    # state = data.data
    state = numpy.copy(data.data)
    distance = 0
    for x in range(4):
        for y in range(4):
            value = state[x][y]
            x_value = x
            y_value = y
            for i in range(4):
                for j in range(4):
                    if(goalNode[i][j] == value):
                        x_goal =  i
                        y_goal = j
            distance += abs(x_value - x_goal) + abs(y_value - y_goal)
    return distance

