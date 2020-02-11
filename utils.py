""" this module store all tools and functions needed for this app"""
from typing import Dict, List

def matchingStrings(sentence : List[str], queries : List[str]) -> Dict[str,int]:
    """
        Method that gives for an array of string as strings in input field the frequency of all the string contained
        in array or strings as queries in input field
        Args:
            - df (pandas.DataFrame): scenario contacts
            - scenario_name (str): scenario name specified in settings file
                                   (in SCENARIO_NAMES variable)
        """
    match_result = dict()
    print(sentence)
    print(queries)
    for word in queries:
        match_result[word] = sentence.count(word)
    print(match_result)
    return match_result
