from nltk.tokenize import WhitespaceTokenizer
from nltk.util import ngrams
from collections import Counter

user_input = input()
f = open(user_input, "r", encoding="utf-8")
corpus = f.read()

tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(corpus)
bigrams = list(ngrams(tokens, 2))

head_dict = {}
for bigram in bigrams:
    head_dict.setdefault(bigram[0], []).append(bigram[1])
for head in head_dict:
    head_dict[head] = Counter(head_dict[head])


while True:
    key = input()
    if key == "exit":
        break
    if key not in head_dict:
        print("Key Error. The requested word is not in the model. Please input another word.")
    else:
        print("Head: {}".format(key))
        for tail in head_dict[key]:
            print("Tail: {} Count: {}".format(tail, head_dict[key][tail]))


def main():
    pass


if __name__ == '__main__':
    main()