#TODO1
name = input("Hello! What is your name?\n")

def borderedMessage(message):
    border = "=" * 80
    print(border)
    print(message)
    print(border)

borderedMessage("Welcome, " + name + ", to the GeoCalc program!")

#Optional: note how this input/while/string-conversion code is repeated later.
# This is a good place to use a function, if you would like extra practice.
#TODO2
def requestNumber(message):
    while True:
        number = input(message)
        try:
            return float(number)
        except ValueError:
            print("INVALID INPUT\n")

def requestSquareSide(n):
    return requestNumber("Please enter the side length for square #" + str(n) + ":\n")

def calculateSquareArea(side):
    return side ** 2

firstSquareArea = calculateSquareArea(requestSquareSide(1))

#TODO3
secondSquareArea = calculateSquareArea(requestSquareSide(2))

#TODO4
def requestTriangleBase(n):
    return requestNumber("Please enter the base of triangle #" + str(n) + ":\n")

def requestTriangleHeight(n):
    return requestNumber("Please enter the height of triangle #" + str(n) + ":\n")

def calculateTriangleArea(base, height):
    return base * height / 2

firstTriangleArea = calculateTriangleArea(requestTriangleBase(1), requestTriangleHeight(1))

#TODO5
secondTriangleArea = calculateTriangleArea(requestTriangleBase(2), requestTriangleHeight(2))

#Print results
print()
print("Your first square area is :", firstSquareArea)
print("Your second square area is :", secondSquareArea)
print("Your first triangle area is :", firstTriangleArea)
print("Your second triangle area is :", secondTriangleArea)
print()

#TODO6
borderedMessage("Goodbye, " + name + ", thank you for using the GeoCalc program!") 
