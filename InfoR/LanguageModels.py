# -*- coding: utf-8 -*-
#	A search engine based on probabilitistic language model of the information retrival.      
#	Author - Janu Verma
#	email - jv367@cornell.edu
#	http://januverma.wordpress.com/
#	@januverma


import sys
from pydoc import help
import os
from collections import defaultdict
from math import log, sqrt
import operator



class LanguageModel:
	"""
	Implements lanuage models for information retrieval.
	Each document in the corpus is a language model and 
	we compute the probability that the query has the 
	same model.  
	"""
	def __init__(self, directory):
		"""
		Arguments:
			directory - Directory of documents to be searched. 
		"""
		self.corpus = os.listdir(directory)
		self.text = {}
		for f in self.corpus:
			f = os.path.join(directory,f)
			with open(f) as doc:
				info = doc.read()
				self.text[f] = info



	def words(self, document):
		"""
		All the words in a document.

		Arguments:
			Document : A textual document. 

		Returns:
			A list containing all the words in the document. 	
		"""
		words = document.split()
		words = [x.lower() for x in words]
		words = [x for x in words if len(x) >= 2and not x.isdigit()]
		return words	


	def word_freq(self, wordlist):
		"""
		Build a dictionary of words with the frequencies of their occurance in the document.

		Arguments:
			Document : A list of all the words in a document.

		Returns:
			A dictionary containing all the words in the document with their frequencies.
				
		"""
		wordFreq = defaultdict(int)
		for w in wordlist:
			wordFreq[w] += 1
		return wordFreq


	def vocabalury(self):
		"""
		All the words in the corpus. 

		Returns:
			A list of al the words in the corpus.
		"""
		allWords = []
		allDocs = self.text
		for d in allDocs.keys():
			d = allDocs[d]
			docWords = self.words(d)
			allWords.extend(docWords)
		return allWords
		
	def wordDict(self):
		"""
		Compute frequencies of occurance of the words in the corpus. 

		Returns:
			A dictionary containing all the words in the corpus with the frequencies
			of their occurance in the whole corpus.
		"""		
		allWords = self.vocabalury()
		return self.word_freq(allWords)



	def document_logScore(self, document, query):
		"""
		Compute the log probability of the query coming from the given document. 

		Arguments:
			
			String document : A textual document. 
			String query : The search query. 

		Returns:
			
			A floating variable logScore	
		"""
		docWords = self.words(document)
		docWordFrequency = self.word_freq(docWords)
		corpusVocablury = self.wordDict()
		normalizingFactor = len(self.vocabalury())

		logProb = 0
		queryWords = self.words(query)
		for q in queryWords:
			try:
				qFreq = docWordFrequency[q]
			except:
				qFreq = 0	
			try:
				 qCount = corpusVocablury[q] 
			except:
				qCount = 0
			alpha = float(qFreq + 1)/float(qCount + normalizingFactor)

			logContribution = log(alpha)
			logProb += logContribution

		return logProb


	def logScoreDict(self, query):
		"""
		Compute the log probability of the query for all the documents.

		Arguments:
			String query: The search query

		Returns:
			A dictionary of all the documents in the corpus with their corresponding logScores.	
		"""	
		rakingDict = defaultdict(float)
		allDocs = self.text 	
		for d in allDocs.keys():
			docText = allDocs[d]
			logScore = self.document_logScore(docText, query)
			rakingDict[d] = logScore
		return rakingDict
		

	def search(self, query, n_docs):
		"""
		Returns documents which are most relavant to the query. 
		Ranking is done by decreasing log probability of the query coming from the document.

		Arguments:
			String query : Search query
			Integer n_docs : Number of matching documents retrived.

		Returns: 
			A list of length n_docs containing documents most relevant to the search query. 
			The list if sorted in the descending order.
		"""	
		relevantDocs = []
		rankings = self.logScoreDict(query)
		rankings = sorted(rankings.iteritems(), key=operator.itemgetter(1), reverse=True)
		for i in range(n_docs):
			u,v = rankings[i]
			relevantDocs.append(u)

		return relevantDocs	










	




