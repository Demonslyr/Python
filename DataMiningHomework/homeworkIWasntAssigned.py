#! python2

from __future__ import print_function
from decimal import Decimal


def importData(filePath):
    f = open(filePath, "r")
    headers = []
    data = []
    for line in f:
        if "<" in line and ">" in line:
            continue
        if "[" in line and "]" in line:
            headers.append(line.translate(None, '[]').strip().split(' '))
            continue
        data.append(line.rstrip('\n').split(' '))
    return [headers, data]

def Symbolicise(data):
    symbols ={}
    distinctSet = []
    attCols = len(data[0])-1
    for column in range(0,attCols):
        for case in data:
            distinctSet.append(float(case[column]))
        distinctSet = sorted(set(distinctSet))
        symbols[str(distinctSet[0])] = str(distinctSet[0]) +".."+str((distinctSet[0]+distinctSet[1])/2)
        for itemIndx in range(1,len(distinctSet)-1):
            symbols[str(distinctSet[itemIndx])] = str((distinctSet[itemIndx]+distinctSet[itemIndx-1])/2) +".."+str((distinctSet[itemIndx]+distinctSet[itemIndx+1])/2)
        symbols[str(distinctSet[len(distinctSet)-1])] = str((distinctSet[len(distinctSet)-1]+distinctSet[len(distinctSet)-2])/2) +".."+str((distinctSet[len(distinctSet)-1]))
        for case in data:
            case[column] = symbols[str(case[column])]

def computePartitionAStar():
    pass

def computePartitionQStar():
    pass

def getSeta():
    pass

def AStarIsLessThanOrEqualToSetDStar(AStar, SetDStar):
    pass

def QStarIsLessThanOrEqualToSetDStar(QStar, SetDStar):
    pass

#U is the data table. 
# Each row is called a case( also an entity). 
# The last column of a row is typically the descision(outcome/result/choice). 
# The subset of all rows that have the same decision are called a concept
def lem1(U, A, SetDStar):
    AStar = computePartitionAStar()
    P = A
    R = 0
    if AStarIsLessThanOrEqualToSetDStar(AStar, SetDStar):
        for a in AStar:
            Seta = getSeta()
            Q = P - Seta
            QStar = computePartitionQStar()
            if QStarIsLessThanOrEqualToSetDStar(QStar, SetDStar):
                P = Q
        R = P
    return R

def main():
    data = importData(r"C:\Users\DrMur\DataMining\Programming Project\test.txt");
    Symbolicise(data[1])
    print(data)
if __name__ == "__main__":
    main()




