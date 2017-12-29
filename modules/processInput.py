import nltk
import spacy
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize, TreebankWordTokenizer, RegexpTokenizer	
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
#import gensim
#from gensim.models import Phrases

nlp = spacy.load('en')

class Input(object):
	"""Class responsibe for Hnadling Input and preprocessing the input"""


	def __init__(self, query, product_id):
		"""
		Initialises the Input object's properties
		:param query:
		:param product_id:
		"""

		self.query = query
		self.product_id = product_id
		self.lower_query = self.caseQuery()
		self.tokens = self.tokenizeQuery()
		self.stemmed_tokens = self.stemQuery(PorterStemmer(),self.tokens)
		self.lemma_tokens = self.lemmatizeQuery(WordNetLemmatizer(),self.tokens)


	def parseInputQuery(self):
		"""
		Parses the Input Query text and returns Parsed query.
		"""

		parsed_query = nlp(self.query)
		return parsed_query


	def caseQuery(self):
		"""
		Lower cases the input query text and returns lower case query
		"""

		lower_case_query = self.query.lower()
		return lower_case_query

	def stemQuery(self,stemmer,tokens):
		"""
		Stems the tokens by removing inflectional forms of the word
		"""

		stemmed_words = []
		for word in tokens:
			stemmed_words.append(stemmer.stem(str(word)))
		return stemmed_words


	def lemmatizeQuery(self,lemmatizer,tokens):
		"""
		Lemmatizes the tokens by removing inflectional forms of the word
		"""

		lemma_words = []
		for word in tokens:
			lemma_words.append(lemmatizer.lemmatize(str(word),pos='n'))
		return lemma_words


	def tokenizeQuery(self):
		"""
		Filtered tokens by removing punctuation and stop words
		"""

		parsed_query = self.parseInputQuery()
		filtered_words = []

		for word in parsed_query:
			if (word.is_punct or word.is_stop or word.like_num or word.is_space):
				pass
			else:
				filtered_words.append(word)
		return filtered_words


	def findSimilarWords(self,word_tokens):
		similar_words = []
		for word in word_tokens:
			syns = wordnet.synsets(str(word))
			if len(syns) > 0:
				for s in syns:
					similar_words.append(s.lemmas()[0].name())
				#words = {syns[i].lemmas()[i].name() for i,j in enumerate(syns) }
				#similar_words.append(words)
		return set(similar_words)


	def similarDocs(self):
		doc1 = nlp(u"can you fit make up brushes in the trays")
		doc2 = nlp(u"No I was not able to fit the make up kit in the trays")
		doc3 = nlp(u"An emu is a large bird.")

		for doc in [doc1, doc2, doc3]:
			for other_doc in [doc1, doc2, doc3]:
				print(doc.similarity(other_doc))


input = Input(u"What are the 100 tray size dimensions please? Height - width - depth (how deep is the tray please). I need to know how deep the trays are because I have some taller items that I'd like to store in the case. It isn't stated. Thank you.",'A10000')
input_tokens = input.tokenizeQuery()

stem_query = input.stemQuery(PorterStemmer(),input_tokens)
lemma_query = input.lemmatizeQuery(WordNetLemmatizer(),input_tokens)

print input.tokens
print input.stemmed_tokens
print input.lemma_tokens

print input.findSimilarWords(input.tokens)