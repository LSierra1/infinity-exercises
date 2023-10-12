wordsList = ["apple", "car", "house", "dog", "cat", "computer", "book", "music", "friend", "sun"]

print(list(filter(lambda moreThan5: len(moreThan5) > 5, wordsList)))