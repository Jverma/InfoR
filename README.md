Information Retrieval in Python
=====

InfoR is a Python package for Information Retrieval. Information retrieval means given a set of (text/html/xml) documents, extract the documents which are most relevant to a seach query. You search engine e.g. Google is a retrieval system. 

InfoR has support for 3 types of retrieval systems : 

1. Vector Space Models
2. Language Models
3. Probabilitistic Models

For more information (no pun intended!) on these models see http://nlp.stanford.edu/IR-book/

Google uses PageRank algorithm which exploits the hyperlinks in an html document. This package currently works only for a corpus of text documents. I'm hoping to add html/xml support also and hopefully include an implementation of PageRank. 

<b>Download :</b> https://pypi.python.org/pypi/infor/

<b>Installation :</b> pip install infor

<b> Dependencies:</b>

1. numpy
2. sklearn (http://scikit-learn.org/stable/)

<b> Usage:</b>

<code>
from InfoR.VectorSpaceModels import VSM, LanguageModel, ProbModel

vector space mode

<code>
out = VSM(corpus)

<code>
out.search(query, number_of_docs_to_be_returned, tf_idf=True, LSA=True, n_comp=3)

language model

<code>
out = LanguageModel(corpus)

<code>
out.search(query, number_of_docs_to_be_returned)

probabistic model

<code>
out = ProbModel(corpus)

<code>
out.search(query, number_of_docs_to_be_returned)
</code>




