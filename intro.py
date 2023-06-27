# Large standard library - pip 
# browsers cannot read python
# natural language/ easy to read 

def say_state(self):
    print(f"My name is Alyssa") 
#Def defines a function named "say_state" that takes on parameter "self". The presence of "self" suggests that this function is part of 

# there is only one equality operator in Python ==
# or - if the first operand is truthy, return it, otherwise return the second operand.
#Python aims to have a clear and straighforward syntax, reducing unneccessary complexity and confusion 

color = input('Enter "green", "yellow", "red"').lower()
print(f"The user entered {color}")

names = ["Tom", "Deborah", "Murray", "Axel"]

for name in names: 
    print(name)

# Ranges - Basic Syntax

for num in range(5): #ranges can only be created by invoking the range() class
    print(num) # the sequence starts at 0 and goes up to, but does not include the integer that is passed in

nums = list(range(10))
print(nums)

letter = input("Please enter a letter from the alphabet").lower()
#check if the entered letter is a vowel 
if letter in ["a", "e", "i", "o", "u"]:
    print("The letter", letter, "is a vowel")
else: 
    print("The letter", letter, "is a consonant")

while True:
    phrase = input("Please enter a word or phrase: ")

    if phrase.lower() == 'quit':
        break 

    length = len(phrase)
    print("What you entered is", length, "characters")

#Ranges - Basic Syntax 

for even in range(2, 10, 2): 
    print(even)

#Ranges can also be used to create lists and tuples:

nums = list(range(10))
print(nums)
odds = tuple(range(1, 10, 2))
