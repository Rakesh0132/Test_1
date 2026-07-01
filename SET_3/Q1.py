text = "a mouse is smaller than a dog but a dog is stronger"
k = 2
words = text.split()
result = []
for i in range(len(words)):
    count = 0
    for j in range(len(words)):
        if words[i] == words[j]:
            count += 1
    if count >= k and words[i] not in result:
        result.append(words[i])
print(result)