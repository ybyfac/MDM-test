""" this module contains the class SparseArray, it represent the structure of the sentence which we querying
    the main goal of an sparseArray is to serialize/synthetize/compress an array full of unintented infos,
    usually zeroes, (at this day) here in our case we defined these unwanted values by only retrieving string values with
    a given query.
"""
import sys

#TODO remove thaht and put it in docker file as ENV


#Complete the matchingStrings function below. DONE
#python -m main ab,abc,bc

#code it DONE
    #relire le code et sa clareté
    #signature
    #pylint
    #mock
    #log?
#dockerize it DONE
#flask_swagger DOING

#add logs
#rename string as sentences of shit like that
#read me 50%
#requierement -> generate it with pip freeze
#mock test
#pylint
#make statement about sonarqube
#execption
#ecrire les signature en entier
#todo faire une classe et faire le main
# decrire le consctructeur
# decrire la methode
from typing import Dict
from utils import matchingStrings


class SparseArray:
    """ class is defined like an array of words as below:
    - sentence a.k.a strings, list of words
    """
    def __init__(self,sentence : str):
        self.sentence = sentence.split(",")
        self.length_sentence = len(sentence)

    def sparse_it(self, query : str) -> Dict[str, int]:
        """
        This method compute frequency in our sentence,
        output we got a dict with our words as key and their frequency as value
        Args:
        - query (str) : list of word to count occurences in our other list of word(a.k.a sentence)
        """
        queries = query.split(",")
        return matchingStrings(self.sentence,queries)


