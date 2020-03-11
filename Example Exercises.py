################################################################################
# Check if a word is a palindrome
################################################################################
#
# racecar = racecar
# taco != ocat
#
# Solution:
#
def testPalindrome(word):
    # Simply check if word is identical to slice of the word reversed
    wordReversed = word[::-1]
    if word == wordReversed:
        return True
    else:
        return False

print("Is 'racecar' a palindrome?\n" +
      str(testPalindrome("racecar")))
print()
print("Is 'taco' a palindrome?\n" +
      str(testPalindrome("taco")))
print("\n")

################################################################################
# Check if a word is an anagram
################################################################################
#
# silent -> listen
# taco ! bell
#
# Solution:
#
def testAnagram(word1, word2):
    # Check if the words are not the same length
    if len(word1) != len(word2):
        return False
    
    # Convert each word into lists of letters
    letters1 = list(word1)
    letters2 = list(word2)

    # Sort the list of letters of each word
    letters1.sort()
    letters2.sort()

    # Check if list of letters of both words are identical
    if letters1 == letters2:
        return True
    else:
        return False

print("Is 'silent' an anagram of 'listen'?\n" +
      str(testAnagram("silent", "listen")))
print()
print("Is 'taco' an anagram of 'bell'?\n" +
      str(testAnagram("taco", "bell")))
print("\n")

################################################################################
# Convert a hexadecimal string to a binary string
################################################################################
#
# F = 1111
# 10 = 00010000
#
# Solution:
#
def hexadecimalToBinary(hexadecimal):
    # Ensure any letters are uppercase
    hexadecimal = hexadecimal.upper()
    
    # Map hexadecimal nibbles to binary bits
    nibblesToBits = {"0":"0000",
                     "1":"0001",
                     "2":"0010",
                     "3":"0011",
                     "4":"0100",
                     "5":"0101",
                     "6":"0110",
                     "7":"0111",
                     "8":"1000",
                     "9":"1001",
                     "A":"1010",
                     "B":"1011",
                     "C":"1100",
                     "D":"1101",
                     "E":"1110",
                     "F":"1111"}

    # Initialize empty string for final result
    binary = ""
    # Iterate through each character in hexadecimal string
    for nibble in hexadecimal:
        # Concatenate next binary bits to current binary string
        binary += nibblesToBits[nibble]

    return binary

print("What is 'F' in binary?\n" + hexadecimalToBinary("f"))
print()
print("What is '10' in binary?\n" + hexadecimalToBinary("10"))
print("\n")

################################################################################
# Convert a timestamp to a readable datetime format
################################################################################
#
# 20200301201134 = March 1, 2020 8:11:34 PM
# 19770527000000 = May 25, 1977 12:00:00 AM
#
# Solution:
#
def convertTimestamp(timestamp):  
    # Map month numbers to month names
    months = {1:"January",
              2:"February",
              3:"March",
              4:"April",
              5:"May",
              6:"June",
              7:"July",
              8:"August",
              9:"September",
              10:"October",
              11:"November",
              12:"December"}
    
    # Extract time fields
    year = timestamp[:4]
    monthNumber = int(timestamp[4:6])
    day = timestamp[6:8]
    hourNumber = int(timestamp[8:10])
    minute = timestamp[10:12]
    second = timestamp[12:]

    # Determine month name
    month = months[monthNumber]

    # Remove leading zero for day, if one exists
    if day[0] == "0":
        day = day[1]

    #
    # Convert 24-hour clock hour to 12-hour clock hour
    #
    
    # Determine if hour is AM or PM
    if hourNumber < 12:
        timeSuffix = "AM"
    else:
        timeSuffix = "PM"

    # Convert hour into range 1-12

    # Explicitly set midnight to 12 as a string
    if hourNumber == 0:
        hour = "12"
    else:
        # Otherwise, use reminder of hour when divided by 12
        hour = hourNumber % 12
        # Convert to string
        hour = str(hourNumber)

    # Concatenate to form date
    date = month + " " + day + ", " + year
    # Concatenate to form time
    time = hour + ":" + minute + ":" + second + " " + timeSuffix
    # Concatenate to form date and time
    dateTime = date + " " + time

    return dateTime

print("What is '20200301201134'?\n" + convertTimestamp("20200301201134"))
print()
print("What is '19770527000000'?\n" + convertTimestamp("19770527000000"))
print("\n")

################################################################################
# Create a histogram to determine top 3 most common values
################################################################################
#
# [1, 2, 3, 2, 1, 2, 2, 1] -> [2, 1, 3]
# ["Jack", "Jill", "John", "Jack", "Jill", "Jack"] = ["Jack", "Jill", "John"]
#
# Solution:
#
def createHistogram(elementList):
    # Create a dictionary named 'histogram'
    histogram = {}
    
    # Iterate through list
    for element in elementList:
        # Check if element already added to histogram
        if element in histogram:
            # Then increment count (value) of element (key)
            histogram[element] += 1
        else:
            # Otherwise, add element (key) to histogram with count (value) of 1
            histogram[element] = 1

    return histogram

def findTopThreeMostCommon(elementList):
    # Generate histogram
    histogram = createHistogram(elementList)

    # Create list to store tuples of top 3 most common elements
    topThree = []

    # Get list of keys in histogram
    keys = list(histogram.keys())
    # Get list of values in histogram
    values = list(histogram.values())
    
    # Add top three most common element
    for i in range(3):
        # Find maximum of values in histogram
        maximum = max(values)
        # Find the index of maximum
        index = values.index(maximum)
        
        # Add maximum element to top three list
        topThree.append(keys[index])

        # Remove maximum as to allow discovery of next maximum
        
        # Remove maximum from values and keys lists
        del values[index]
        del keys[index]

    return topThree
                

print("What are the top three most common elements of:\n" +
      "[1, 2, 3, 2, 1, 2, 2, 1]\n" +
      str(findTopThreeMostCommon(
          [1, 2, 3, 2, 1, 2, 2, 1])))
print()
print("What are the top three most common elements of:\n" +
      '["Jack", "Jill", "John", "Jack", "Jill", "Jack"]\n' +
      str(findTopThreeMostCommon(
          ["Jack", "Jill", "John", "Jack", "Jill", "Jack"])))
print("\n")
