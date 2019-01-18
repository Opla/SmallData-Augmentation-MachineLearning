# Text augmentation for Machine Learning tasks: 
# How to grow your text dataset for classification?


This is the implementation of some of data augmentation techniques we explained in our blog article
https://medium.com/opla/text-augmentation-for-machine-learning-tasks-how-to-grow-your-text-dataset-for-classification-38a9a207f88d

Text augmentation is a technique used when the training data is not enough to achieve accurate performance on machine learning tasks. The goal here is to extend the text data by creating new similar content.

words_shuffling.py allows to dirsupt the order of a sentence words to create a new senteence.

word_replacement.py allows to replace some words of each sentence with a similar word, a synonym in this case. 

Synonyms are listed in ppdb-xl.txt extracted from http://paraphrase.org/#/ . 

Requirements:
  - NLTK
  

