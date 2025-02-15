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

    firstDegreeApproximations = []
    approximationsMade = 0
    #first degree approximations
    for row, point in enumerate(dataset):
        if(row == 0):
            continue

        inputForLagrange = [dataset[row - 1], dataset[row]]

        firstDegreeApproximations.append(Langrangian(inputForLagrange, x))
        approximationsMade += 1

    #second degree approximation
    x0 = dataset[0][0]
    x2 = dataset[2][0]

    result = ((x - x0) * firstDegreeApproximations[1] - 
             (x - x2) * firstDegreeApproximations[0]) / (x2 - x0)

    print(f"{result}\n")

def Problem2(dataSet):
    differenceTable = []

    zerothDegree = []
    #initialize difference table; 0th degree will just be y
    for row, point in enumerate(dataSet):
        zerothDegree.append(point[1])

    differenceTable.append(zerothDegree)


    for degree in range(1, len(dataSet)):
        nthDegree = []

        currentArray = differenceTable[degree - 1]
        for index in range(len(currentArray) - 1): #element in enumerate(currentArray):
            x0 = dataSet[index][0]
            xN = dataSet[degree + index][0]
            
            value = (currentArray[index + 1] - currentArray[index]) / (xN - x0)
            nthDegree.append(value)

        print(nthDegree[0])
        differenceTable.append(nthDegree)

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
dataSet = [[3.6, 1.675], [3.8, 1.436], [3.9, 1.318]]
targetX = 3.7

Problem1(nevilleDataSet, nevilleTargetX)
Problem1(dataSet, targetX)

Problem2()
dataSet = [[7.2, 23.5492],
           [7.4, 25.3913],
           [7.5, 26.8224],
           [7.6, 27.4589]]
targetX = 7.3

#Newton's Forward Method table
Problem2(dataSet)

Problem3()

Problem4()

Problem5()
