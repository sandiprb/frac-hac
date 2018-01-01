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
		self.lower_query = self.__case_query()
		self.tokens = self.__tokenize_query()
		self.stemmed_tokens = self.__stem_query(PorterStemmer(), self.tokens)
		self.lemma_tokens = self.__lemmatize_query(WordNetLemmatizer(), self.tokens)
		self.words = self.__find_similar_words()

	def extract_pid(self):
		"""
		Extracts Product Id from Raw Query
		:return:
		"""
		pid = re.findall(r"[A-Z0-9]{10}", self.query)
		return pid

	def __parse_input_query(self):
		"""
		Parses the Input Query text and returns Parsed query.
		:return:
		"""
		parsed_query = nlp(self.query)
		return parsed_query

	def __case_query(self):
		"""
		Lower cases the input query text and returns lower case query
		"""
		lower_case_query = self.query.lower()
		return lower_case_query

	def __stem_query(self, stemmer, tokens):
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

	def __lemmatize_query(self, lemmatizer, tokens):
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

	def __tokenize_query(self):
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

	def __find_similar_words(self):
		"""
		Finds similar words for keywords using wordnet's lexicons DB
		:return:
		"""
		similar_words = []
		for word in self.tokens:
			syns = wordnet.synsets(str(word))
			if len(syns) > 0:
				for s in syns:
					similar_words.append(s.lemmas()[0].name())
		similar_words = set(similar_words)
		additional_words = {s for s in similar_words if s not in self.tokens}
		return list(additional_words) + self.tokens