import random

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
    # choose a random word as the first word of the chain
    first_word = random.choice(list(head_dict.keys()))
    # choose the second word based on the counts of the tails of the first word, repeat until 10 words in the chain
    chain = random.choices(list(head_dict[first_word].keys()), weights=list(head_dict[first_word].values()), k=9)

    sentence_list.append(first_word)
    sentence_list.extend(chain)
    sentence = " ".join(sentence_list)

    return sentence


def main():
    # generate 10 sentences
    for i in range(10):
        print(generate_sentence())


if __name__ == '__main__':
    main()
