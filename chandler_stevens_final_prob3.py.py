quantity = int(input("Type and Enter how many heights will be entered: "))
count = 0
heightsSum = 0

for count in range(quantity):
    heightsSum += float(input("Type and Enter the height in meters: "))
    count += 1

print("The average height of all",quantity,"people is",(heightsSum/quantity),"meters.")

##height = 0
##sumHeights = 0
##total = 0
##
##while height >= 0:
##    height = float(input("Type and Enter the height in meters: "))
##    if height >= 0:
##        sumHeights += height
##        total += 1
##
##print("The average height of all",total,"people is",(sumHeights/total),"meters.")

##chandler_stevens_final_prob3.txt
##Type and Enter how many heights will be entered: 4
##Type and Enter the height in meters: 1.88
##Type and Enter the height in meters: 2.03
##Type and Enter the height in meters: 2.28
##Type and Enter the height in meters: 1.8
##The average height of all 4 people is 1.9974999999999998 meters.

##Type and Enter the height in meters: 1.88
##Type and Enter the height in meters: 2.03
##Type and Enter the height in meters: 2.28
##Type and Enter the height in meters: 1.8
##Type and Enter the height in meters: -1
##The average height of all 4 people is 1.9974999999999998 meters.
