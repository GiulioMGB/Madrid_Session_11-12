with open("book.txt") as file:
    text = file.read()
file.close()

# create a dictionary of word frequencies
word_freq = {}
punctuation = ",.'!?;-()\n"

file = open("book.txt")
for line in file:
    # remove punctuation
    for p in punctuation:
        line = line.replace(p, "")
    words = line.split(" ")
    for word in words:
        word = word.lower()
        if len(word) < 4:
            continue
        # check and add into dictionary
        if word in word_freq:
            # words in dictionary increase by 1
            word_freq[word] += 1
        else:
            word_freq[word] = 1

frequencies = list(word_freq.values())
frequencies.sort(reverse=True)
top_frequencies = frequencies[:10]
print(top_frequencies)


# match the word
for top_word in top_frequencies:
    for key in word_freq:

        if word_freq[key] == top_word:
            print(f"Word '{key}' appears {top_word} times")
            break
file.close()
