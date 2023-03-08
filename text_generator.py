from nltk.tokenize import WhitespaceTokenizer

user_input = input()
f = open(user_input, "r", encoding="utf-8")
corpus = f.read()

tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(corpus)

print("Corpus statistics")
print("All tokens: ", len(tokens))
print("Unique tokens: ", len(set(tokens)))

while True:
    index = input()
    if index == "exit":
        break
    try:
        index = int(index)
        if index >= len(tokens):
            print("Index Error. Please input an integer that is in the range of the corpus.")
        else:
            print(tokens[index])
    except ValueError:
        print("Type Error. Please input an integer.")


def main():
    pass


if __name__ == '__main__':
    main()