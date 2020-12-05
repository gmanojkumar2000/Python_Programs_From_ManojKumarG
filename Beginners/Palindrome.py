#Reversing a string and checking palindrome or not

import string

word = input("Enter the string to be reversed:")
reversed_word=word[::-1]
print("The reverse of "+str(word)+" is "+str(reversed_word))

if word == reversed_word:
    print(word+" is a palindrome!!!")
else:
    print(word + " is not a palindrome!!!")
