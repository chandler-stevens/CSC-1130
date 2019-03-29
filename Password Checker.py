username = input("Enter username: ")
password = input("Enter password: ")
print()

score = 0

#test for length in pw
if len(password) >= 8:
    print("+1pt for password length of 8 or above")
    score += 1
else:
    print("Warning: password is too short!")
print()

#test for digits in pw
hasDigits = False
for char in password:
    if char.isdigit():
        hasDigits = True
        break

if hasDigits:
    print("+1pt for numbers in password.")
    score += 1
else:
    print("Warning: no numbers in password!")

print()

#test for uppercase in pw
hasUpper = False
for char in password:
    if char.isupper():
        hasUpper = True
        break

if hasUpper:
    print("+1pt for uppercase letters in password.")
    score += 1
else:
    print("Warning: no uppercase letters in password!")
print()

#test for symbols in pw
if not(password.isalnum()):
    print("+1pt for using a symbol in password.")
    score += 1
else:
    print("Warning: no symbols in password!")
print()

#test for username in pw
if not(username in password):
    print("+1pt for username NOT being in password.")
    score += 1
else:
    print("Warning: username is in password!")
print()

print("Your password score is: ", score)
if score >= 4:
    print("This is a strong password!")
elif score >= 2:
    print("This is a moderate password.")
else:
    print("This is a weak password.")
