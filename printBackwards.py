def printBackwards (userWord):
    return userWord[::-1]


userWord = input("Please enter a word that you would like to see spelled backwards: ")

wordBackwards = printBackwards(userWord)

print(wordBackwards)