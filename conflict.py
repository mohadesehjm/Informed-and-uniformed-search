import numpy as numpy

rootNode = [[13, 14, 15, 0],
           [9, 10, 11, 12],
           [5, 6, 7, 8],
            [1, 2, 3, 4]]
def confilict (data):
    arr = numpy.copy(data)
    currentNumber = 0
    count = 0
    add = 4
    numConfilict = 0
    check = 0
    # horizontal
    for i in range(12) :
        currentNumber += 1
        if(currentNumber % 4 == 0):
            currentNumber += 1
            add += 4
        count = currentNumber
        # مکان گره ی در حال بررسی
        for i in range(4):
            for j in range(4):
                if arr[i][j] == currentNumber:
                    num1_i = i
                    num1_j = j
                    break
        while count < add :
            # مکان با شماره های بعدی
            count += 1
            for i in range(4):
                for j in range(4):
                    if arr[i][j] == count:
                        num2_i = i
                        num2_j = j
                        check = 1
                        break
            if num1_i is num2_i and check:
                if num1_j > num2_j :
                    numConfilict += 1
            check = 0

    # vertical
    currentNumber = 0
    check = 0
    for i in range(12) :
        currentNumber += 1
        count = currentNumber
        # مکان گره ی در حال بررسی
        for i in range(4):
            for j in range(4):
                if arr[i][j] == currentNumber:
                    num1_i = i
                    num1_j = j
                    break
        while count < 13 :
            # مکان با شماره های بعدی
            count += 4
            for i in range(4):
                for j in range(4):
                    if arr[i][j] == count:
                        num2_i = i
                        num2_j = j
                        check = 1
                        break
            if num1_j is num2_j and check:
                if num1_i > num2_i :
                    numConfilict += 1
            check = 0
    numConfilict *= 2
    return numConfilict


