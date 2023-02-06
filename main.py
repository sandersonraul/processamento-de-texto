import string
import time
import pandas as pd
import nltk

stopwords = set(nltk.corpus.stopwords.words("portuguese"))

def word_count(filename, words_to_search):
    with open(filename, encoding="utf-8") as f:
        text = f.read()
        
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    words = [word.lower() for word in text.split() if word.lower() not in stopwords]
    
    word_frequency = pd.Series(words).value_counts().to_dict()
    common_word = max(word_frequency, key=word_frequency.get)
    
    word_frequency_searched = {}
    word_positions = {}
    for word in words_to_search:
        word_to_compare = word.lower()
        word_frequency_searched[word] = word_frequency.get(word_to_compare, 0)
        word_positions[word] = [i for i, w in enumerate(words) if w == word_to_compare]
    
    return word_frequency_searched, common_word, word_frequency[common_word], word_positions

filename = input()
words_to_search = input().split(",")

start_time = time.time()
word_frequency_searched, common_word, count, word_positions = word_count(
    filename, words_to_search
)

for word in words_to_search:
    print(f"# {word}")
    print(f"Frequência: {word_frequency_searched[word]}")
    print(f"Posições: {', '.join(str(p) for p in word_positions[word])}")
    print()

print(f"#{common_word}")
print(f"Frequência:  {count}")
print(f"Tempo de execução: {time.time() - start_time:.2f} segundos.")
