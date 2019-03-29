###Problem 1 example solution

name = input("Please enter your name: ")
print("Hello", name)

EPS = 8.854E-12 #in Farads/meter

perm = float(input("Enter the relative permeability: "))
area = float(input("Enter the area of your capacitor (meters^2): "))
distance = float(input("Enter the distance between the plates (meters) "))

cap = perm * EPS * (area/distance)

print("The capacitance is:", cap, " Farads")

###Problem 2 example solution
standing = int(input("Enter class standing: "))

if standing < 4:
    if standing < 3:
        print("Meet with your advisor")
    else:
        print("Get an internship!")
else:
    print("Apply to graduate!")
    
print("Thanks for using CounselorBot")

###Problem 3 example solution
total = 0
numEntries = 0

height = float(input("Please enter a height to average (-1 to stop):"))

while height >= 0.0:
    total += height
    numEntries += 1
    height = float(input("Please enter a height to average (-1 to stop):"))

if numEntries > 0:
    average = total/numEntries
    print("The average height is:", average)
else:
    print("No data entered!")


###Problem 4 example solution
def printTabbed(printChar, numSpaces):
    print(" " * numSpaces, end="")
    print(printChar)

j = 0
for i in "Merry Christmas":
    printTabbed(i, j)
    j += 1
