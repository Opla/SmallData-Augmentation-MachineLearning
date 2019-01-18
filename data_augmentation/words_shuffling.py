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
