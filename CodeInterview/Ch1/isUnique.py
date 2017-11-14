import string
import time

testString_1 = "Hello"
testString_2 = "Yes"
testString_3 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+~`,./;'[]\{}|:<>??"

def areCharsUnique(inputString):
    if len(inputString) > 128:
        return False
    for character in inputString:
        if len(inputString.split(character, 2)) > 2:
            return False
    return True

def stillAreCharsUnique(inputString):
    if len(inputString) > 128:
        return False
    return len(inputString) == len(set(inputString))

def main():
    start = time.time()
    print(areCharsUnique(testString_1))
    end = time.time()
    print(end - start)
    start = time.time()
    print(areCharsUnique(testString_2))
    end = time.time()
    print(end - start)
    start = time.time()
    print(areCharsUnique(testString_3))
    end = time.time()
    print(end - start)
    print("");
    start = time.time()
    print(stillAreCharsUnique(testString_1))
    end = time.time()
    print(end - start)
    start = time.time()
    print(stillAreCharsUnique(testString_2))
    end = time.time()
    print(end - start)
    start = time.time()
    print(stillAreCharsUnique(testString_3))
    end = time.time()
    print(end - start)
    return 0

if __name__ == "__main__":
    main()
