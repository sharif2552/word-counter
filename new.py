# reading fromt the file 
file = open("filename.txt", "r")
content = file.read()
words = content.split()
words = [word.lower() for word in words]
file.close()

#my word list that is goint to be used for searching
wordlist=["Python", "JavaScript", "Java", "C++", "C#", "Ruby", "a","b"]
wordlist = [word.lower() for word in wordlist]

print("Converted every item to lowercase\n")
word_count = {}
for searchword in wordlist:
    word_count[searchword] = 0
    for word in words:
        if searchword==word: 
            if searchword in word_count:
                word_count[searchword] += 1
            else:
                word_count[searchword] = 1

for word in word_count:
    print(word +" = "+str(word_count[word]) )