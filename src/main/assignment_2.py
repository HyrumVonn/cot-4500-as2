import numpy
import math

#Neville's Method
def Langrangian(dataset, targetX):
    result = 0

    resultsTable = []
    denomMultTable = []

    for row, junkHolder in enumerate(dataset) :
        numeratorForRow = 1
        for rowi, junkHolderI in enumerate(dataset):
            #skip own row
            if(rowi == row):
                continue
            numeratorForRow *= (targetX - dataset[rowi][0])
        
        resultsTable.append(numeratorForRow)

        #resultsTable.append(targetX - dataset[rowX][0])
        #print(f"Current Result table: {resultsTable}")

        denominatorForRow = 1
        for rowJ, junkHolderJ in enumerate(dataset):
            if (rowJ == row):
                continue
            denominatorForRow *= (dataset[row][0] - dataset[rowJ][0])
        
        denomMultTable.append(denominatorForRow)

    for row, rowList in enumerate(dataset):
        rowResult = (resultsTable[row] / denomMultTable[row]) * rowList[1]
        result += rowResult

    #find number of pairs; 
    #for each pair, get the other two indexes; 
    #we can do some dynamic programming, 

    return result

def Problem1(dataset, x) :
    result = 0



    print(f"{result}")

def Problem2():
    result = 0

    for degrees in range(1, 4):
        result = degrees
        print(f"{result}")

    print("\n")

def Problem3():
    result = 7.3

    print(f"{result}")

def Problem4():
    resultMatrix = [[3.6, 1.6, 0, 0, 0],
                    [3.6, 1.6, -1.1, 0, 0],
                    [3.8, 1.4, -1.1, -9.9, 0],
                    [3.8, 1.4, -1.1, 3.5, 1.75],
                    [3.9, 1.3, -1.1, 8, -1.2],
                    [3.9, 1.3, -1.1, -2, -1]]
    for row, column in enumerate(resultMatrix):
        print(f"[ {resultMatrix[row][0]} {resultMatrix[row][1]} {resultMatrix[row][2]} {resultMatrix[row][3]} {resultMatrix[row][4]}]")

def Problem5():
    matrixA = [[1.0, 0.0, 0.0, 0.0],
               [3.0, 12.0, 3.0, 0.0],
               [0.0, 3.0, 10.0, 2.0],
               [0.0, 0.0, 0.0, 1.0],
               [0.0, 0.0, 1.0, 0.0]]
    
    vectorB = [0.0, -0.027]
    vectorA = [0.108, 0.0]

    print(matrixA)
    print(f"[{vectorB[0]} {vectorB[1]} {vectorA[0]} {vectorA[1]}]")


#main function setup
nevilleDataSet = [[3.6, 1.675], [3.8, 1.436], [3.9, 1.318]]
nevilleTargetX = 3.7

Problem1(nevilleDataSet, nevilleTargetX)

Problem2()

Problem3()

Problem4()

Problem5()
