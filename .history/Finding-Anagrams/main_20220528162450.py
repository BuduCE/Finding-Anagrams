# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    #First step is to input first word
    word = input("Enter 1st word: ")
    #Second step is to input the second word
    anagram = input("Enter your second word: ")

    #Sorting individual variable
    sorted_word1 = sorted(word)
    sorted_word2 = sorted(anagram)

    #Conditional statement to compare the two words entered
    if sorted_word1 == sorted_word2:
        print("True");
    else:
        print("False");
    return True
print (wors)

