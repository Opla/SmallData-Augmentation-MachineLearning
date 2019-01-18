#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2015-present, CWB SAS

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.

__author__ = "Maali Mnasri"
__copyright__ = "Copyright (c) 2015-present, CWB SAS - All Rights Reserved"
"""
    
from nltk import word_tokenize
from nltk.corpus import stopwords

stoplist = stopwords.words('english')


def get_synonyms_lexicon(path):
    synonyms_lexicon = {}
    text_entries = [l.strip() for l in open(path).readlines()]
    for e in text_entries:
        e = e.split(' ')
        k = e[0]
        v = e[1:len(e)]
        synonyms_lexicon[k] = v
    return synonyms_lexicon


def synonym_replacement(sentence, synonyms_lexicon):
    keys = synonyms_lexicon.keys()
    words = word_tokenize(sentence)
    n_sentence = sentence
    for w in words:
        if w not in stoplist:
            if w in keys:
                n_sentence = n_sentence.replace(w, synonyms_lexicon[w][0])  # we replace with the first synonym
    return n_sentence


if __name__ == '__main__':
    text = 'Many customers initiated a return process of the product as it was not suitable for use.' \
           'It was conditioned in very thin box which caused scratches on the main screen.' \
           'The involved businesses positively answered their clients who were fully refunded.'
    sentences = text.split('.')
    sentences.remove('')
    print sentences
    synonyms_lexicon = get_synonyms_lexicon('./ppdb-xl.txt')
    for sentence in sentences:
        new_sentence = synonym_replacement(sentence, synonyms_lexicon)
        print '%s' % sentence
        print '%s' % new_sentence
        print '\n'
