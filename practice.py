# Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal 
#substring
#consisting of non-space characters only.

s = "Hello World" #setting our s variable to a string
words = s.split() #Split the string into a list of words
last_word = words[-1] #access the last word in the list 
print(last_word) #output: "world"

#the string 's' is split into a list of words using split(), resulting list is ["Hello", "World"]. By using 'words[-1]', we access the last element in the list, which is "World". This gives us the last word in the original string. 
#split() method does not require any arguments or objects. By default, if no delimiter is specified, it splits the string at whitespace characters(spaces, tabes, and newlines)

#Write a function to find the longest common prefix string amonst an array of strings
#If there is no common prefix, return an empty string ""

#Define the "longestCommonPrefix" function that takes a list of strings (`strs`) as input. 
def longestCommonPrefix(strs): 
   
   #check if the input list is empty. if it is, return an empty string, as there are no strings to find a common prefix among. 
   if not strs: 
      return "" 
   #if the input list is empty, return an empty string
   
   #Zip the strings together and iterate over the characters
   for i, chars in enumerate(zip(*strs)):
      if len(set(chars)) > 1:
      
        return min(strs)


