name = input("Type and Enter your name: ")
print("Hello "+name+"!")
EPS = 8.8534e-12
perm = float(input("Type and Enter the number of the relative permittivity of the dielectric: "))
area = float(input("Type and Enter the cross-sectional area of the plates in meters squared: "))
distance = float(input("Type and Enter the distance between the plates in meters: "))
cap = perm*EPS*(area/distance)
print("The capacitance of the parallel plate capacitor is",cap,"Farads.")

##chandler_stevens_final_prob1.txt
##Type and Enter your name: Me
##Hello Me!
##Type and Enter the number of the relative permittivity of the dielectric: 2
##Type and Enter the cross-sectional area of the plates in meters squared: 1.5
##Type and Enter the distance between the plates in meters: 2.2
##The capacitance of the parallel plate capacitor is 1.207281818181818e-11 Farads.
