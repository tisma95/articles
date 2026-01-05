#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Projet: Native similarity of sentences          #
#               Version: V1                                     #
#               File: native_similarity.py                      #
#################################################################

"""
   Ask two sentences to the user and analyse the similarities between them.
"""

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize

lemmatizer = WordNetLemmatizer()

from typing import List
from string import punctuation
from math import sqrt

# Téléchargement des ressources nécessaires
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

def getSentence(index: int) -> str:
    """
        Name
        -----
        getSentence

        Parameters
        ----------
        :param index(required int): The number of the sentence to ask.

        Response
        --------
        User input.

        Example
        -------
        getSentences(1) => ask "Enter the sentence 1:"
    """
    response = ""
    while response.strip() == "":
        response = input(f"Enter the sentence {index}:")
        if response.strip() == "":
            print("\nYou need to enter a sentence, please !\n")
    return response

def getSentenceWords(sentence: str) -> List[str]:
    """
        Name
        -----
        getSentenceWords

        Parameters
        ----------
        :param sentence(required str): The target sentence.

        Response
        --------
        List of words of the sentence without punctuations.

        Example
        -------
        getSentenceWords("The cat eats the mouse.") => will return ["the", "cat", "eats", "the", "mouse"]
    """
    # Remove all punctations in sentence
    filterSentence = sentence
    for puncLetter in punctuation:
        if puncLetter in filterSentence:
            filterSentence = filterSentence.replace(puncLetter, '')
    # Remove the trailling space
    filterSentence = filterSentence.rstrip()
    # Get the unic word and return it
    response = [word.lower() for word in filterSentence.split()]
    return response

def getCleanupSentence(sentence: str) -> str:
    """
        Name
        -----
        getCleanupSentence

        Parameters
        ----------
        :param sentence(required str): The target sentence to cleanup.

        Description
        -----------
        Remove all punctuations letters in sentences and set in lower case and return it.

        Response
        --------
        Cleanup sentence.

        Example
        -------
        getCleanupSentence("The cat eats the mouse.") => The cat eats the mouse
    """
    response = []
    for word in sentence.split():
        # Delete the punctuation in word
        for letter in punctuation:
            if letter in word:
                word = word.replace(letter, '')
        response.append(word.strip())
    return ' '.join(response)

# Utility fonction to specify the right pos tag for lemma not noun by default
def getWordnetOfWordPostag(tag):
    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN

if __name__ == "__main__":
    print("\n\tSIMILARITY WITH NLTK\n")
    # Get the input from the user
    sentence1 = getSentence(1)
    sentence2 = getSentence(2)
    # Filter the user inputs
    inputSentence1 = getCleanupSentence(sentence=sentence1)
    inputSentence2 = getCleanupSentence(sentence=sentence2)
    # Tokenize the sentences
    token1 = word_tokenize(inputSentence1)
    token2 = word_tokenize(inputSentence2)
    print("\nThe tokens of sentence 1 words:")
    print(token1)
    print("\nThe tokens of sentence 2 words:")
    print(token2)
    # Create the postag of word
    postag1 = pos_tag(token1)
    postag2 = pos_tag(token2)
    print("\nThe postag of sentence 1 words:")
    print(postag1)
    print("\nThe postag of sentence 2 words:")
    print(postag2)
    # Lemmatizer the words
    lemma1 = [lemmatizer.lemmatize(word, getWordnetOfWordPostag(tag)) for word, tag in postag1]
    lemma2 = [lemmatizer.lemmatize(word, getWordnetOfWordPostag(tag)) for word, tag in postag2]
    print("\nThe lemma of sentence 1 words:")
    print(lemma1)
    print("\nThe lemma of sentence 2 words:")
    print(lemma2)
    # Create the corpus
    corpus = lemma1 + lemma2
    corpus = list(set(corpus))
    # Calculate the similarity
    supValue = 0
    infValue1 = 0
    infValue2 = 0
    for word in corpus:
        supValue += lemma1.count(word) * lemma2.count(word)
        infValue1 += lemma1.count(word)**2
        infValue2 += lemma2.count(word)**2
    infValue = sqrt(infValue1) * sqrt(infValue2)
    similarity = supValue/infValue
    print("\nThe result of similarity with spacy internal similarity is:\n")
    print(f"Sentence 1: {sentence1}")
    print(f"Sentence 2: {sentence2}")
    print(f"Similarity: cos(alpha)={similarity:.2f} or {similarity:.2%}")

# Exemple de lemmatisation
words = ["running", "bought", "better", "cats", "run"]
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

print(lemmatized_words)  # ['running', 'bought', 'better', 'cat']