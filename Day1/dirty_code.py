# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 20:31:25 2019.

@author: Winchester
"""

import logging
import math
import re
from collections import Counter
from py2neo import Graph
import json
from bottle import Bottle
from cherrypy.wsgiserver import CherryPyWSGIServer

WORD = re.compile(r'\w+')

logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S')

loGger = logging.getLogger(__name__)

def getCosine(vec1, vec2):
    """Extract two parameters is a cosine function.
    
    It takes one input"""
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    s = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


class Query(object):
    """This class does something."""
    
    def __init__(self, ip_addr, username, password):
        """This is just the constructor.
        and it initializes."""
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        self.graph = Graph(self.ip_addr, username=self.username, password=self.password)

    def Code_to_Synonym(self, disease_code):
        logger.info("Matching the disease code from its synonym : ", disease_code)
        query = ''' MATCH (co:Code{CodeID:"%s"}) - [:is_known] -> (dis:Synonym)
                    RETURN DISTINCT dis.Is_known
                ''' % (disease_code)

        result = self.graph.run(query)
        logger.info("Disease code matched to its synonym")
        print(result)
        return result

    def Synonym_to_Code(self, disease_name):
        logger.info("Matching synonym from the disease code: ", disease_name)
        query = ''' MATCH (syn:Synonym{Is_known:"%s"}) <-[:is_known] - (disease:Code)
                    RETURN DISTINCT disease.CodeID
                ''' % (disease_name)

        result = self.graph.run(query)
        logger.info("Synonym matched to its code")
        return result

    def code_to_parent(self, disease_code):
        logger.info("Returning all the parents of the disease code: ", disease_code)
        query = ''' MATCH(:Code{CodeID:"%s"}) - [:is_child_of*] -> (parent:Code)
                    RETURN DISTINCT parent.CodeID
                ''' % (disease_code)
        result = self.graph.run(query)
        logger.info("Parents of the disease code returned")
        return result

    def code_to_child(self, disease_code):
        logger.info(" Returning all the immediate children of a disease code : ", disease_code)
        query = ''' MATCH(:Code{CodeID:"%s"}) <- [:is_child_of] - (child:Code)
                    RETURN DISTINCT child.CodeID
                ''' % (disease_code)

        result = self.graph.run(query)
        logger.info(" Immediate children of the disease code returned ")
        return result

    def word_to_code(self, word):
        logger.info("Exact matching from the [:is_known] relation of the word : ", word)
        query = ''' MATCH (Disease:Synonym)
                    WHERE Disease.Is_known contains "%s"
                    MATCH (Disease:Synonym {Is_known : Disease.Is_known}) <- [:is_known] - (disease:Code)
                    WHERE disease.CodeID IS NOT NULL
                    RETURN DISTINCT Disease.Is_known, disease.CodeID
                ''' % (word)

        result = self.graph.run(query)
        logger.info(" Returned the disease code and disease synonyms of the given word")
        return result

    def code_to_frequent_codes(self, disease_code):
        query = ''' MATCH (code:Code{CodeID:"%s"})
                    MATCH p=(code:Code)-[r:occurs_with]->(code1:Code)
                    RETURN code1.CodeID
                    ORDER BY r.weight DESC
                    limit 3
                ''' % (disease_code)

        result = self.graph.run(query)
        return result
