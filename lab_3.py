from natasha import Segmenter, NewsEmbedding, NewsMorphTagger, NewsSyntaxParser, Doc
from nltk import sent_tokenize


def norm(txt):
    _, x = map(int, txt.split('_'))
    return x


path = "dataset.txt"
file = open(path, "r", encoding="utf8")


segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)


words = dict()
tree = {}

lines = file.readlines()
sents = []


for line in lines:
    sentences = sent_tokenize(line)
    for i in range(len(sentences)):
        sents.append(sentences[i])


def compute(ind):
    text = sents[ind]
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    root_id = 0
    sent = doc.sents[0]
    tokens = [token for token in sent.tokens if token.id]
    for token in tokens:
        norm_id = norm(token.id)
        words[norm_id] = token.text
        if token.rel == 'root':
            root_id = norm_id

    for i in words.keys():
        if i != 0:
            tree[i] = []

    for token in sent.tokens:
        norm_id = norm(token.id)
        norm_head_id = norm(token.head_id)
        if (norm_head_id != 0):
            tree[norm_head_id].append(norm_id)
    return doc, root_id


def print_result(doc, a):
    def lrep(a):
        s = '('
        s += words[a]
        if len(tree[a]) > 0:
            for t in tree[a]:
                s += lrep(t)
        s += ')'
        return s

    def rrep(a):
        s = '('

        if len(tree[a]) > 0:
            for t in tree[a]:
                s += lrep(t)
        s += words[a]
        s += ')'
        return s

    print('root:', words[a])
    print('words:', words)
    print('tree:', tree)
    doc.sents[0].syntax.print()
    print('left:', lrep(a))
    print('right:', rrep(a))
    print(doc.tokens)


def main():
    for i in range(5):
        doc, a = compute(i)
        print_result(doc, a)
        print()


if __name__ == "__main__":
    main()
