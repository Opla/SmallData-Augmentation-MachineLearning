from nltk import word_tokenize
import random


def augment(sentence,n):
    new_sentences = []
    words = word_tokenize(sentence)
    for i in range(n):
        random.shuffle(words)
        new_sentences.append(' '.join(words))
    new_sentences = list(set(new_sentences))
    return new_sentences


nsentences = augment("my new year resolution is to perfect many things as the main solution",10)
for s in nsentences:
    print s
