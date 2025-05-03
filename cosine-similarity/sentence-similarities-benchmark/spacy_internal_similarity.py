####################################################################################
#               Author: Ismael Maurice                                             #
#               Language: Python                                                   #
#               Projet: Similarity of sentences with Spacy function similarity     #
#               Version: V1                                                        #
#               File: spacy_internal_similarity.py                                 #
####################################################################################


"""
   Ask two sentences to the user and analyse the similarities between them by using the formula with lemme.
"""

import spacy

from string import punctuation

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

if __name__ == "__main__":
    print("\n\tSPACY INTERNAL SIMILARITY\n")
    # Get the input from the user
    sentence1 = getSentence(1)
    sentence2 = getSentence(2)
    # Filter the user inputs
    inputSentence1 = getCleanupSentence(sentence=sentence1)
    inputSentence2 = getCleanupSentence(sentence=sentence2)
    # Tokenize the sentences
    nlp = spacy.load("en_core_web_lg")
    # Tokenize the sentences
    token1 = nlp(inputSentence1)
    token2 = nlp(inputSentence2)

    # Calculate the similarity
    similarity = token1.similarity(token2)
    print("\nThe result of similarity with spacy internal similarity is:\n")
    print(f"Sentence 1: {sentence1}")
    print(f"Sentence 2: {sentence2}")
    print(f"Similarity: cos(alpha)={similarity:.2f} or {similarity:.2%}")
