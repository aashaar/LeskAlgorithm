# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 22:46:36 2019

@author: aashaar
"""
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords as sw

    
def leskDisambiguate(word, sentence):
    #Get all senses from wordnet & assign 1st one as best:
    wordSenses = wn.synsets(word)
    #print(wordSenses[0].definitions())
    bestSense = wordSenses[0]
    #print(best_sense.definition())
    #Tokenize the sentence:
    context = set(wt(sentence))
    maxOverlap = 0
    
    for sense in wordSenses:
        signature = getSignature(sense)
        overlap = computeOverlap(signature, context)
        if overlap > maxOverlap:
            maxOverlap = overlap
            bestSense = sense
    return bestSense

def getSignature(sense):
    #Returns tokens of sense's definition & examples:
    definitionTokens = set(wt(sense.definition()))
    for example in sense.examples():
        definitionTokens.union(set(wt(example)))
    return definitionTokens

def computeOverlap(signature, context):
    #Conputes the overlaps between signature & context and returns the length of overlaps set:
    signatureTokens = signature.difference(set(sw.words('english')))
    #print(signatureTokens)
    #print("==================================")
    overlapsSet = signatureTokens.intersection(context)
    return len(overlapsSet)


if __name__ == '__main__':
    word = "bank"
    sentence = "The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities."
    finalSense = leskDisambiguate(word, sentence)
    print("========================================\nThe Best Sense is: " + str(finalSense))
    print("\nDefinition: " + str(finalSense.definition()))
    print("\nExample: " + str(finalSense.examples()))
