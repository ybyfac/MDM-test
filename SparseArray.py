""" this module contains the class SparseArray, it represent the structure of the sentence which we querying
    the main goal of an sparseArray is to serialize/synthetize/compress an array full of unintented infos,
    usually zeroes, (at this day) here in our case we defined these unwanted values by only retrieving string values with
    a given query.
"""

from typing import Dict
from utils import matchingStrings

class SparseArray:
    """ class is defined like an array of words as below:
    - sentence a.k.a strings, list of words
    """
    def __init__(self,sentence : str):
        # this could be __private attributes and add getter and setter to the class
        # also SparseArray could implements an interface contract
        # this way we could have multiple implementation of SparseArray
        # for this test we keep it simple
        self.sentence = sentence
        self.length_sentence = len(sentence)

    def sparse_it(self, query : str) -> Dict[str, int]:
        """
        This method compute frequency in our sentence,
        output we got a dict with our words as key and their frequency as value
        Args:
        - query (str) : our query contains filters,
        list of word to count occurences in our other list of word (a.k.a sentence)
        """
        return matchingStrings(self.sentence,query)


