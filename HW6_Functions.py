#TODO1
WELCOME =("Welcome to the GeoClac program!")

def geoCalc(message) :
    border = "="*50
    print (border)
    print ("Welcome", message +"!")
    print (border)

geoCalc("Welcome to the GeoClac program!")

#Optional: note how this input/while/string-conversion code is repeated later.
# This is a good place to use a function, if you would like extra practice.
#TODO2
squareSideString = input("Please enter the side length for your 1st square: ")

while not squareSideString.isdigit():
    squareSideString = input("Please enter the side length for your 1st square: ")

squareSide = int(squareSideString)

def squareArea(sideLength) :
    return (sideLength)**2

firstSquareArea = squareArea(squareSide)



#TODO3
squareSideString2 = input("Please enter the side length for your 1st square: ")

while not squareSideString2.isdigit():
    squareSideString2 = input("Please enter the side length for your 1st square: ")

squareSide2 = int(squareSideString2)

secondSquareArea = squareArea(squareSide2)



#TODO4
triangleBaseString = input("Please enter the base for your 1st triangle: ")

while not triangleBaseString.isdigit():
    triangleBaseString = input("Please enter the base for your 1st triangle: ")
    
triangleHeightString = input("Please enter the height for your 1st triangle: ")

while not triangleHeightString.isdigit():
    triangleHeightString = input("Please enter the height for your 1st triangle: ")

triangleBase = float(triangleBaseString)
triangleHeight = float(triangleHeightString)

def triangleArea(base,height) :
    return (base * height / 2)
firstTriangleArea = triangleArea(triangleBase, triangleHeight)



#TODO5

triangleBaseString2 = input("Please enter the base for your 2nd triangle: ")

while not triangleBaseString2.isdigit():
    triangleBaseString2 = input("Please enter the base for your 2nd triangle: ")
    
triangleHeightString2 = input("Please enter the height for your 2nd triangle: ")

while not triangleHeightString2.isdigit():
    triangleHeightString2 = input("Please enter the height for your 2nd triangle: ")

triangleBase2 = float(triangleBaseString2)
triangleHeight2 = float(triangleHeightString2)

secondTriangleArea = triangleArea(triangleBase2, triangleHeight2)


#print results
print()
print("Your first square area is :", firstSquareArea)
print("Your second square area is :", secondSquareArea)
print("Your first triangle area is :", firstTriangleArea)
print("Your second triangle area is :", secondTriangleArea)
print()

#TODO6

geoCalc("Goodbye, thank you for using the GeoCalc program!") 


