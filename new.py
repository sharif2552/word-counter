
file = open("filename.txt", "r")

content = file.read()
words = content.split()
file.close()


word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in word_count:
    print(word + " = " + str(word_count[word]) + " times")
