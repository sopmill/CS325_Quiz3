def printBackwards (userWord):
    return userWord[::-1]


userWord = input("Please enter a word: ")

wordBackwards = printBackwards(userWord)

print(wordBackwards)