import random
import string

from nltk.tokenize import WhitespaceTokenizer
from nltk.util import ngrams
from collections import Counter

# read the corpus
user_input = input()
f = open(user_input, "r", encoding="utf-8")
corpus = f.read()

# generate bigrams
tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(corpus)
bigrams = list(ngrams(tokens, 2))

# generate a markov model
head_dict = {}
for bigram in bigrams:
    head_dict.setdefault(bigram[0], []).append(bigram[1])
for head in head_dict:
    head_dict[head] = Counter(head_dict[head])


# generate a sentence
def generate_sentence():
    sentence_list = []
    # choose a random word as the first word of the chain, and starts with a capital letter
    uppercase_letters = list(string.ascii_uppercase)
    capital_head = list(filter(lambda word: word[0] in uppercase_letters, head_dict.keys()))
    # not start with a word that ends with a sentence-ending punctuation mark
    capital_head_end = list(filter(lambda word: not word.endswith((".", "!", "?")), capital_head))
    first_word = random.choice(capital_head_end)
    sentence_list.append(first_word)
    # always end with a sentence-ending punctuation mark，and should not be shorter than 5 tokens
    while True:
        last_word = sentence_list[-1]
        if last_word.endswith((".", "!", "?")) and len(sentence_list) >= 5:
            break
        else:
            next_word = random.choices(list(head_dict[last_word].keys()),
                                       weights=list(head_dict[last_word].values()))[0]
            sentence_list.append(next_word)

    sentence = " ".join(sentence_list)

    return sentence


def main():
    # generate 10 sentences
    for i in range(10):
        print(generate_sentence())


if __name__ == '__main__':
    main()
