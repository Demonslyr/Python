def urlIfyString(inputString):
    return inputString.replace(' ','%20')

def main():
    print(urlIfyString("Hello world    see spaces?"))

if __name__ == "__main__":
    main()