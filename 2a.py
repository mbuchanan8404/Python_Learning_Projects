###############################
# Matthew Ryan Buchanan
# problem set 2a
###############################


#1
print("Hello World"[8])


#2
print("thinker"[2:5])


#2b
s = 'hello'
print(s[1])


#3
s = 'Sammy'
print(s[2:])


#4
# If you meant return a list of each letter in Mississippi
print([letter for letter in "Mississippi"])

# Or did you mean...

# Turn Mississippi into a set and return only unique letters
print("".join(set("Mississippi"))[::-1])


#5
def detect_palindromes():
    lst_of_phrases = []
    num_of_phrases = int(input("Enter the number of phrases to check:\n"))
    for x in range(num_of_phrases):
        lst_of_phrases.append((''.join(filter(str.isalpha, input("Input a word or phrase:")))).lower())
    for phrase in lst_of_phrases:
        if phrase == phrase[::-1]:
            print("Y")
        else:
		print("N")
        
detect_palindromes()
