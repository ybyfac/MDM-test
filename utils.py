""" this module store all tools and functions needed for this app"""
from typing import Dict, List
import logging
from logging.handlers import RotatingFileHandler

# Logging settings
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

def matchingStrings(sentence : str, query : str) -> Dict[str,int]:
    """
        Method that gives all occurences in a sentence for a given query,
        only return occurences of strings contained in that query, like a filter
        Args:
            - sentence (str) : strings, chain of strings separated with a simple comma
            - query (str): scenario name specified in settings file
    """

    match_result = dict()
    sentence = sentence.split(",")
    queries = query.split(",")

    logger.debug('STRING :: %s',sentence)
    logger.debug('QUERY :: %s',queries)
    for word in queries:
        match_result[word] = sentence.count(word)
    print(match_result)
    return match_result
