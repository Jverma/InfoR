# -*- coding: utf-8 -*-

#	A search engine based on Vector Space model of the information retrival. 
#	Also has the option to do Latent Sementic Indexing of the term-document matrix.     
#	Author - Janu Verma
#	email - jv367@cornell.edu
#	http://januverma.wordpress.com/
#	@januverma


import sys
from pydoc import help
import os


import numpy as np 


try:
	from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
	from sklearn.decomposition import TruncatedSVD 
	from sklearn.metrics.pairwise import cosine_similarity
	from sklearn.preprocessing import Normalizer
except:
	print "Error : Requires scikit-learn."
	sys.exit()



class VSM:
	"""
	Implements a Vector space search engine. Each document is represented by a vector in a high dimensional 
	vector space where there is a dimension corresponding to each unique word in the corpus. 
	The contents of the vector are the frequencies or tf-idf scores of the term. 

	Latent Sementic Analysis (LSA) of the term-document matrix is performed by Singular Value Decomposition (SVD). 
	A is the term-document matrix where each row corresponds to a row and each term is a column.
	The entries of the matrix a_ij contains the tf-idf score of the term i in document j.
	The SVD maps each document from term space to the (lower dimensional) concept space. 
	"""

	def __init__(self, directory):
		"""
		Arguments:
			directory : Directory of documents to be searched. 
		"""
		self.corpus = os.listdir(directory)
		self.text = []
		for f in self.corpus:
			f = os.path.join(directory,f)
			with open(f) as doc:
				info = doc.read()
				self.text.append(info)

				

	def search(self, q, n_docs, tf_idf=False, LSA=False, n_comp=None):
		""" 
		Returns documents which are most relavant to the query. 
		Ranking is done by decreasing cosine similarity with the query. 


		Arguments:
			String q : Search query
			Integer n_docs : Number of matching documents retrived. 
			Boolean tf_idf : If True, the vector features will have tf-idf scores. 
			Boolean LSA : If True, the vectors will be mapped to a low dimenional concept space. 
			Integer n_comp : Number of components for the LSA, dimension of the concept space. 


		Returns:
			A list of length n_docs containing documents most relevant to the search query. 
			The list if sorted in the descending order. 
		"""

		##	Default vector have entries the frequencies of occurance of the terms. 
		vectorizer = CountVectorizer(min_df=0,stop_words='english')
		
		##	Vectors with entries as tf-idf scores. 
		if (tf_idf == True):
			vectorizer = TfidfVectorizer(min_df=0, stop_words='english')
		
		X = vectorizer.fit_transform(self.text)
		X = X.toarray()

		##	vectorize the query accordingly. 
		query = [q]
		query = vectorizer.transform(query)
		query = query.toarray()

		##	Reduce the vectors to to n_comp - dimensional vector space. 
		if (LSA == True):
			if (n_comp != None): 
				lsa = TruncatedSVD(n_components=n_comp)
				X = lsa.fit_transform(X)
				X = Normalizer(copy=False).fit_transform(X)
				query = lsa.transform(query)

		#print query
		ranking = cosine_similarity(X,query)
		doc_id = np.argsort(ranking, axis=0)
		doc_id = doc_id[::-1]
		ranked_docs = [self.corpus[doc_id[i][0]] for i in range(n_docs)]
		return ranked_docs
		
	
	def help(self):
		"""
		Description of the class and the methods. 
		"""
		return help(VSM)


			








