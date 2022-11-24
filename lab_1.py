from nltk import download
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import sent_tokenize

path = "dataset.txt"

download('stopwords')


def printSentences(text):
    count = 1
    print('\n\nПредложения: \n')
    for el in text:
        sentences = sent_tokenize(el)
        for i in range(len(sentences)):
            print(str(count) + ": " + str(sentences[i]))
            count += 1
    file.close()


def printWordsFromSentences(text):
    sentNum = 1
    print('\n\nСлова из предложений: \n')
    for el in text:
        sentences = sent_tokenize(el)
        for i in range(len(sentences)):
            sent = sentences[i]
            words = word_tokenize(sent)
            words = [word for word in words if word.isalpha()]
            print(str(sentNum) + ":", *words)
            sentNum += 1
    file.close()


def printStopWords():
    print('\n\nСтоп слова: \n')
    print(*stopwords.words('russian'))


def printSentencesWithoutStopWords(text):
    count = 1
    st_words = set(stopwords.words('russian'))
    print('\n\nСлова из предложений без стоп слов: \n')
    for el in text:
        sentences = sent_tokenize(el)
        for i in range(len(sentences)):
            sent = sentences[i]
            words = word_tokenize(sent)
            without_stop_words = [
                word for word in words if not word.lower() in st_words and word.isalpha()]
            print(str(count) + ":", *without_stop_words)
            count += 1
    file.close()


def printWordsRate(text):
    sent = text
    result_list = []
    stop_words = set(stopwords.words('russian'))
    print('\n\nРейтинг слов:')
    for word1 in sent:
        tmp = word1
        words = word_tokenize(tmp)
        words_without_stop = [
            word.lower() for word in words if not word in stop_words and word.isalpha()]
        for word in words_without_stop:
            result_list.append(word)
    map = {}

    for word in result_list:
        if word in map.keys():
            map[word] += 1
        else:
            map[word] = 1

    print()
    sortedList = {k: v for k, v in sorted(
        map.items(), key=lambda item: (-item[1], item[0]))}

    for word in sortedList:
        print(sortedList[word], word)
    file.close()


file = open(path, "r", encoding="utf8")
text = file.readlines()
stopWords = set(stopwords.words('russian'))

printSentences(text)
printWordsFromSentences(text)
printStopWords()
printSentencesWithoutStopWords(text)
printWordsRate(text)
