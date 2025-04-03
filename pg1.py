from collections import Counter

def word_count(text):
    words = text.split()
    return Counter(words)

print(word_count("hello world hello"))  