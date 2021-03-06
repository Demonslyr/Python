def normalShiftCompare(stringInQuestion, stringToCompareAgainst):
    for x in range(0,len(stringInQuestion)-1):
        if stringInQuestion[x+1:len(stringInQuestion)]+stringInQuestion[0:x+1] == stringToCompareAgainst:
            return True
    return False

def mirroredStringShiftCompare(stringInQuestion, stringToCompareAgainst):
    return normalShiftCompare(stringInQuestion[::-1], stringToCompareAgainst)

def isPermutation(stringInQuestion, stringToCompareAgainst):
    if stringInQuestion == stringToCompareAgainst:
        return True
    return sorted(stringInQuestion) == sorted(stringToCompareAgainst)

def main():
    print(isPermutation("Hello", "leHol"))
    print(isPermutation("Hello", "eHllo"))
    print(isPermutation("Hello", "leHl"))
    

if __name__ == "__main__":
    main()