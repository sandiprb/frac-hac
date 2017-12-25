import nltk
import spacy
from nltk.tokenize import word_tokenize, TreebankWordTokenizer, RegexpTokenizer	
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
#import gensim
#from gensim.models import Phrases

nlp = spacy.load('en')


class Input(object):
	"""docstring for ClassName"""
	

	def __init__(self, query, product_id):
		self.query = query
		self.product_id = product_id
		self.lower_query = self.caseQuery()


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


	# def tokenizeQuery(self,tokenizer):
	# 	"""
	# 	Breaks the input query into tokens using tokenizer passed
	# 	"""
	# 	tokens = tokenizer(self.lower_query)
	# 	return tokens


	def stemQuery(self,stemmer,tokens):
		"""
		Stems the tokens by using the concept of Stemming
		"""
		stemmed_words = []
		for word in tokens:
			stemmed_words.append(stemmer.stem(word))
		return stemmed_words


	def lemmatizeQuery(self,lemmatizer,tokens):
		"""
		Lemmatizes the tokens by using the concept of Lemmatizing
		"""
		lemma_words = []

		for word in tokens:
			lemma_words.append(lemmatizer.lemmatize(word,pos='n'))
		return lemma_words


	def tokenizeQuery(self):
		"""
		Filtered tokens by removing punctuation and stop words
		"""
		parsed_query = self.parseInputQuery()

		filtered_words = []

		for word in parsed_query:
			if word.is_punct or word.is_stop:
				pass
			else:
				filtered_words.append(word)
		return filtered_words


input = Input(u"What are the tray size dimensions please? Height - width - depth (how deep is the tray please). I need to know how deep the trays are because I have some taller items that I'd like to store in the case. It isn't stated. Thank you.",'A10000')
#input_tokens = input.tokenizeQuery(word_tokenize)

#filtered_tokens = input.filterTokens(input_tokens)
print input.query
#print input_tokens
#print filtered_tokens
print input.tokenizeQuery()
