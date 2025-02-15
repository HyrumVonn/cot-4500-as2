#test to find desired precision to use on Newton-Raphson
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

        differenceTable.append(nthDegree)

    return differenceTable

def Problem3(dataset, x):
    #get the diffTable from problem 2
    diffTable = Problem2(dataset)

    pTable = []

    #p0 is 
    pTable.append(dataSet[0][1])

    #fill out each p: get the coefficient, multiply it by (x - x0)...(x - xK-1)
    for degree in range(1, len(dataSet)):
        pPrev = pTable[degree - 1]
        pCurrent = diffTable[degree][0]
        print(f"{pPrev} + {pCurrent}")
        for i in range(degree):
            #retrieve every x indexed below the current degree (i.e., for degree 1, only x0, but
            #for degree 2, x0 & x1)
            print(f" * ({x} - {dataSet[i][0]})")
            pCurrent = pCurrent * (x - dataSet[i][0])

        print()

        pTable.append(pPrev + pCurrent)
    
    result = pTable[len(pTable) - 1]
    print(f"{result}\n")


def PrintApproximationMatrixForP4(matrix):
    for i in range(len(matrix[0])):
        rowString = "["
        for j in range(len(matrix)):
            if(type(matrix[j][i]) == type(1.3)):
                if(matrix[j][i] < 0) :
                    rowString = rowString + f"{matrix[j][i]:.8E} "
                else :
                    rowString = rowString + f" {matrix[j][i]:.8E} "
            else :
                rowString = rowString + f" {matrix[j][i]}  "
        print(f"{rowString}]")

    print()


def Problem4(dataSet):
    approximationMatrix = []

    xValues = []
    for element in dataSet :
        #append each x and f(x) twice; then, for f'(x), 
        xValues.append(element[0])
        xValues.append(element[0])
    approximationMatrix.append(xValues)

    fXValues = []
    for element in dataSet :
        #append each x and f(x) twice; then, for f'(x), 
        fXValues.append(element[1])
        fXValues.append(element[1])
    approximationMatrix.append(fXValues)

    
    #used to mark which cells to go through in degree 1, and recalculate
    placeHolderString = "FILL IN LATER"
    fdXValues = []
    for row, element in enumerate(dataSet) :
        if(row == 0):
            fdXValues.append(0.0)
        else :
            fdXValues.append(placeHolderString)
        
        fdXValues.append(element[2])
    approximationMatrix.append(fdXValues)

    #checking that it's working out, remove
    PrintApproximationMatrixForP4(approximationMatrix) 
    #in actual program

    #the 1st degree requires a special case: going through, and only replacing the "Fill in Later"
    for index, val in enumerate(approximationMatrix[2]) :
        if(val != placeHolderString):
            continue

        x0 = approximationMatrix[0][index-1]
        xN = approximationMatrix[0][index]

        degree = 2
        approximationMatrix[2][index] = (approximationMatrix[degree - 1][index] - 
                                         approximationMatrix[degree - 1][index - 1]) / (xN - x0)
        
    #from the 2nd degree onward, treat as normal Divided Difference
    for degree in range(2, len(xValues)):
        nthDegree = []
        for i in range(degree) :
            nthDegree.append(0.0)

        for index in range(degree, len(xValues)):
            x0 = approximationMatrix[0][index - degree]
            xN = approximationMatrix[0][index]

            #normally, it'd be approxMat[degree - 1]... but due to including the x as element 0 
            #in the approx matrix, degree 1 was treated as degree 2, and so on; indexing adjusted 
            #accordingly
            val = (approximationMatrix[degree][index] - 
                   approximationMatrix[degree][index - 1]) / (xN - x0)
            nthDegree.append(val)
        approximationMatrix.append(nthDegree)

    PrintApproximationMatrixForP4(approximationMatrix)
        


def PrintP2DataSet(dataSet):
    for index in range(1, len(dataSet)):
        print(dataSet[index][0])
    print()

testMatrix = [[2.0, 0.6931],
              [2.2, 0.7885],
              [2.3, 0.8329]]
x = 2.1

Problem1(testMatrix, x)

print("Page 15 of slides (program example):")
dataSet = [[1, .7651977],
           [1.3, .6200860],
           [1.6, .4554022],
           [1.9, .2818186],
           [2.2, .1103623]]

PrintP2DataSet(Problem2(dataSet))

print("Page 14 of Slides (the example beginning with (8.1, 16.9)...)")
dataSet = [[8.1, 16.94410],
           [8.3, 17.56492],
           [8.6, 18.50515],
           [8.7, 18.82091]]

PrintP2DataSet(Problem2(dataSet))
Problem3(dataSet, 8.4)

print("Problem3 Data given: ")
dataSet = [[7.2, 23.5492],
           [7.4, 25.3913],
           [7.5, 26.8224],
           [7.6, 27.4589]]

#Newton's Forward Method table
diffTable = Problem2(dataSet)

targetX = 7.3
Problem3(dataSet, targetX)

dataSet = [[1.3, .6200860, -.5220232],
           [1.6, .4554022, -.5698959],
           [1.9, .2818186, -.5811571]]
Problem4(dataSet)

dataSet = [[3.6, 1.675, -1.195],
           [3.8, 1.436, -1.188],
           [3.9, 1.318, -1.182]]

Problem4(dataSet)
