# -*- coding: utf-8 -*-

#	A search engine based on probabilitistic models of the information retrival.      
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


class ProbModel:
	"""
	Implements probabilitistic models for information retrieval. 
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
			document : A textual document. 

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
			document : A list of all the words in a document.

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
			A list of all the words in the corpus.
		"""
		allWords = []
		allDocs = self.text
		for d in allDocs.keys():
			d = allDocs[d]
			docWords = self.words(d)
			allWords.extend(docWords)
		return allWords	



	def doc_freq(self):
		"""
		Compute the document frequency of all the terms in the corpus.

		Returns:
			A dictionary of all the terms in the corpus with their document frequency.
		"""
		allWords = self.vocabalury()
		allWords = set(allWords)
		allDocs = self.text
		docFreq = defaultdict(int)
		for x in allWords:
			for d in allDocs.keys():
				d = allDocs[d]
				docTerms = self.words(d) 
				if (x in docTerms):
					docFreq[x] += 1
		return docFreq



	def docScore(self, document, query, k, b):
		"""
		Compute the log odds ratio of the document being relevant to the query.
		Arguments:
			
			document : A textual document. 
			query : The search query. 
			k : tuning parameter for term frequency.
			b : tuning parameter for for document length.

		Returns:
			
			A floating variable score
		"""

		# total number of docs
		n = len(self.corpus)

		# words in the document
		docText = self.words(document)

		# length of the document
		l = len(docText)

		# average length of a document
		l_av = float(len(self.vocabalury()))/n

		# document frequency dict
		df = self.doc_freq()

		# words in the document
		tokens = self.words(document)

		#term frequency dict
		tf = self.word_freq(tokens)

		# inittalize the score for the document
		score = 0

		# query
		queryWords = self.words(query)

		for x in queryWords:
			try:
				tf_x = tf[x]
			except:
				continue
			try:
				df_x = df[x]
			except:
				continue

			# inverse document frequency of the term.	
			idf = log(n/df_x)	

			# correction factor
			correction = float((k + 1)*(tf_x))/(k*(1-b) + b*(l/(l_av)) + (tf_x))

			# total contribution 
			contribution = idf * correction
			score += contribution

		return score	
					




	def ranking(self, query, k, b):
		"""
		Ranking of the documents based on their relevance to the query. 

		Arguments:
			query: The search query

		Returns:
			A dictionary of all the documents in the corpus with their corresponding relevance odds ratio.	
		"""
		if (k != None):
			k = k
		else:
			k = 0	
		if (b != None):
			b = b
		else:
			b = 0	

		documents = self.text
		rankingDict = defaultdict(float)
		for d in documents.keys():
			docText = documents[d]
			score = self.docScore(docText, query, k, b)
			rankingDict[d] = score
		return rankingDict	


	def search(self, query, n_docs, k=None, b=None):
		"""
		Returns documents which are most relavant to the query. 
		Ranking is done by decreasing odds ratio for the document to be relevant for the query. 

		Arguments:
			String query : Search query
			Integer n_docs : Number of matching documents retrived.
			Float k : tuning parameter for term frequency, (0<=k<=1). 
					A value of 0 corresponds to a binary model (no term frequency), 
					and a large value corresponds to using raw term frequency
			Float b: tuning parameter for for document length,  (0<=b<=1).  
					b = 1 corresponds to fully scaling the term weight by the document length, 
					while b = 0 corresponds to no length normalization.		

		Returns: 
			A list of length n_docs containing documents most relevant to the search query. 
			The list if sorted in the descending order.
		"""	
		if (n_docs > len(self.corpus)):
			n_docs = len(self.corpus)

		relevantDocs = []
		if (k != None):
			k = k
		if (b != None):
			b = b	
		rankings = self.ranking(query, k, b)
		rankings = sorted(rankings.iteritems(), key=operator.itemgetter(1), reverse=True)
		for i in range(n_docs):
			u,v = rankings[i]
			relevantDocs.append(u)
		return relevantDocs	





























