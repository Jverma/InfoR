import sys
from InfoR.VectorSpaceModels import VSM
from InfoR.LanguageModels import LanguageModel
from InfoR.ProbabilitisticModels import ProbModel


def Corpus():
	print "The default data set is the corpus of my answers on Quora." 
	print "The answers can be seen at https://www.quora.com/Janu-Verma-2/answers"
	print "I answer questions on a varied range of topics and this would a good example for text analytics. "

Corpus()
directory = "Data"

# Search Query
q = "mathematical physicist edward witten"
print "The search query is - " + q


#	Number of docs to be retrieved 
n_docs = 5
print "Number of documents to be retrieved - " + str(n_docs)


def vsm():
	
	out = VSM(directory)
			
	print "Search Results based on Frequency Counts : \n"   
	print out.search(q,n_docs)

	print "Search Results based on tf-idf vectors : \n"   
	print out.search(q,n_docs, tf_idf=True)

	print "Search Results based on tf-idf after performing LSA : \n"  
	print "The number of LSA compnents is 3." 
	print out.search(q,n_docs, tf_idf=True, LSA=True, n_comp=3)




def LM():
	out = LanguageModel(directory)

	print "Search Results from Language Models: \n"
	print out.search(q,n_docs)


def LM():
	out = ProbModel(directory)

	print "Search Results from Probabilitistic Models: \n"
	print out.search(q,n_docs)	





























