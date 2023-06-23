'''

Define a function to count the frequency of words in a given list of words.
'''


def count_word_frequency(words):
    word_count = dict()
    unique = list(set(words))
    for word in unique:
        word_count[word] = words.count(word)
    return word_count

# Alternative solution
# def count_word_frequency(words):
#     word_count = {}
#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1
#     return word_count


wordList = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(wordList))
