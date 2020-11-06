translation = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
}

def sumTheAras(listOfArabics):
  theSum = 0
  for arabic in listOfArabics:
    theSum = theSum + arabic
  return theSum


# this is a bit weird but stay with me on this one...
# we loop through all the arabic numbers backwards
# we check each number to see if it's bigger than the number before it
# if it is then we subtract the previous value from the number in question
# we then flag to ignore the previos number in the next iteration of the loop
# get it?

# i've ignored edge cases. Sue me.
def dealWithSubtractions(listOfArabics):
  subtractionsDealtWithNumerals = []
  skipNext = False
  # forgive me. Aparently reduce functions aren't readable so have been 
  # banned from pyhton 3 :-0
  for index in range(len(listOfArabics)):
    if skipNext: 
      subtractionsDealtWithNumerals.insert(0, 0)
      skipNext = False
      continue
    currentNumber = listOfArabics[len(listOfArabics) - index - 1]

    # if it's the first number, just at that to our array. Ain't no subtraction here
    if not index == len(listOfArabics) - 1:
      previousNumber = listOfArabics[len(listOfArabics) - index - 2]
      # if the number is bigger than the one before it then we need to subtract!
      if (currentNumber > previousNumber):
        subtractionsDealtWithNumerals.insert(0, currentNumber - previousNumber)
        # flag up that previous number doesn't need to be processed
        skipNext = True
      else: subtractionsDealtWithNumerals.insert(0, currentNumber)
    else: subtractionsDealtWithNumerals.insert(0, currentNumber)
  return subtractionsDealtWithNumerals


def romanToAra (a):
  return translation[a]


# i could totally do more here
def validatInput(input):
  isValid = True
  isValid = isinstance(input, str)
  if not isValid :
    print("No! given variable is not an instance of type string")
    return False
  
  # check if the characters in the string are actual roman numerals

  return isValid


# feed me a roman numeral please
def convert(numerals: str):
  # validate
  isValid = validatInput(numerals)
  if not isValid:
    return False
  
  # split the string into individual parts
  listOfNumerals = list(numerals)
  convertedListOfNumerals = list(map(romanToAra ,listOfNumerals))
  subsDealthWithNumerals = dealWithSubtractions(convertedListOfNumerals)
  yourLovelyArabicNumber = sumTheAras(subsDealthWithNumerals)
  print(listOfNumerals)
  print(convertedListOfNumerals)
  print(subsDealthWithNumerals)
  print(yourLovelyArabicNumber)

  return yourLovelyArabicNumber
