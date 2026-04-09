word = input("Enter the word: ")

count = {}
for letter in word:
    count[letter] = count.get(letter, 0) + 1

print(count)