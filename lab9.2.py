
keywords = {"example", "keyword", "programming", "python", "development", "english", "learning"}

uniqueKeywords = set()
    
for word in keywords:
    uniqueWord = ''.join(sorted(set(word), key=word.index))
    uniqueKeywords.add(uniqueWord)

print(uniqueKeywords)