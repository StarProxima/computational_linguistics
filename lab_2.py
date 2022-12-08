from nltk import word_tokenize
from nltk import sent_tokenize
from pymorphy2 import MorphAnalyzer

path = "dataset.txt"
file = open(path, "r", encoding="utf8")

text = file.readlines()
words = []
file.close()


def wordsFromSentences():
    for line in text:
        sentences = sent_tokenize(line)
        for i in range(len(sentences)):
            words.extend(word_tokenize(sentences[i]))


def morphAnalyze():
    morph = MorphAnalyzer()
    for i in range(50):
        print("Слово " + str(i) + ": " + words[i])
        print(str(morph.parse(words[i])))
        print()


def main():
    wordsFromSentences()
    morphAnalyze()


if __name__ == "__main__":
    main()
