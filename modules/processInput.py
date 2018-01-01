import re

import spacy
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet

nlp = spacy.load('en')

class Input(object):
	"""Class responsible for Handling Input and Preprocessing the input"""

	def __init__(self, query):
		"""
		Initialises the Input object's properties
		:param query:
		:param product_id:
		"""
		self.query = query
		self.product_id = self.extract_pid()
		self.lower_query = self.caseQuery()
		self.tokens = self.tokenizeQuery()
		self.stemmed_tokens = self.stemQuery(PorterStemmer(), self.tokens)
		self.lemma_tokens = self.lemmatizeQuery(WordNetLemmatizer(), self.tokens)

	def extract_pid(self):
		"""
		Extracts Product Id from Raw Query
		:return:
		"""
		pid = re.findall(r"[A-Z0-9]{10}", self.query)
		return pid

	def parseInputQuery(self):
		"""
		Parses the Input Query text and returns Parsed query.
		:return:
		"""
		parsed_query = nlp(unicode(self.query))
		return parsed_query

	def caseQuery(self):
		"""
		Lower cases the input query text and returns lower case query
		"""
		lower_case_query = self.query.lower()
		return lower_case_query

	def stemQuery(self, stemmer, tokens):
		"""
		#Stems the tokens by removing inflectional forms of the word
		:param stemmer:
		:param tokens:
		:return:
		"""
		stemmed_words = []
		for word in tokens:
			stemmed_words.append(stemmer.stem(str(word)))
		return stemmed_words

	def lemmatizeQuery(self, lemmatizer, tokens):
		"""
		Lemmatizes the tokens by removing inflectional forms of the word
		:param lemmatizer:
		:param tokens:
		:return:
		"""
		lemma_words = []
		for word in tokens:
			lemma_words.append(lemmatizer.lemmatize(str(word), pos='n'))
		return lemma_words

	def tokenizeQuery(self):
		"""
		Filtered tokens by removing punctuation and stop words
		:return:
		"""
		parsed_query = self.parseInputQuery()
		filtered_words = []

		for word in parsed_query:
			if (word.is_punct or word.is_stop or word.like_num or word.is_space):
				pass
			else:
				filtered_words.append(str(word))
		return filtered_words

	def findSimilarWords(self):
		"""
		Finds similar words for keywords using wordnet's lexicons DB
		:return:
		"""
		similar_words = []
		for word in self.tokens:
			syns = wordnet.synsets(str(word), 'n')
			if len(syns) > 0:
				for s in syns:
					similar_words.append(s.lemmas()[0].name())
		similar_words = set(similar_words)
		additional_words = {s for s in similar_words if s not in self.tokens}
		return additional_words	