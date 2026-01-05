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

from typing import List
from string import punctuation
from math import sqrt

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

if __name__ == "__main__":
    print("\n\tNATIVE SIMILARITY CALCULATING\n")
    # Get the input text
    sentence1 = getSentence(1)
    sentence2 = getSentence(2)
    # Create the dico of words
    sentence1Words = getSentenceWords(sentence=sentence1)
    sentence2Words = getSentenceWords(sentence=sentence2)
    dico = sentence1Words + sentence2Words
    dico = list(set(dico))
    # Build the vector of each sentences
    vSentence1 = [sentence1Words.count(word) for word in dico]
    vSentence2 = [sentence2Words.count(word) for word in dico]
    print("Sentence 1 vector:", vSentence1)
    print("Sentence 2 vector:", vSentence2)
    # Calculate the similarity with formula
    supResult = sum([vSentence1[i]*vSentence2[i] for i in range(len(dico))])
    infResult = sqrt(sum([vSentence1[i]*vSentence1[i] for i in range(len(dico))])) * sqrt(sum([vSentence2[i]*vSentence2[i] for i in range(len(dico))]))
    similarity = supResult/infResult
    print("\nThe result of similarity with native Python code is:\n")
    print(f"Sentence 1: {sentence1}")
    print(f"Sentence 2: {sentence2}")
    print(f"Similarity: cos(alpha)={similarity:.2f} or {similarity:.2%}")
