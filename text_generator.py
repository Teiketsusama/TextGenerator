from nltk.tokenize import WhitespaceTokenizer
from nltk.util import ngrams

user_input = input()
f = open(user_input, "r", encoding="utf-8")
corpus = f.read()

tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(corpus)
bigrams = list(ngrams(tokens, 2))

print("Number of bigrams: ", len(bigrams))

while True:
    index = input()
    if index == "exit":
        break
    try:
        index = int(index)
        if index >= len(bigrams):
            print("Index Error. Please input a value that is not greater than the number of all bigrams.")
        else:
            print("Head: {} Tail: {}".format(bigrams[index][0], bigrams[index][1]))
    except ValueError:
        print("Type Error. Please input an integer.")


def main():
    pass


if __name__ == '__main__':
    main()