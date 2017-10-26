
text = input("Text: ")
word_total = text.split()

known_words = {}

for word in word_total:
    word_amount = known_words.get(word, 0)
    if word_amount is None:
        known_words[word] = 1
    else:
        known_words[word] = word_amount + 1

word_total = list(known_words.keys())
word_total.sort()
print(word_total)
max_length = max((len(word) for word in word_total))

for word in word_total:
    print("{:{}} : {}".format(word, max_length, known_words[word]))