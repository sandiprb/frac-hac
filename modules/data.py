import glob
import gzip
import re

import pandas as pd
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer


class Data(object):
	"""Reads and holds the dataset from the compressed files."""

	def __init__(self, folder_path='../data/', filetype='*.gz'):
		self.path = glob.glob(folder_path + filetype)
		self.questions, self.reviews = self.get_data

	@property
	def get_data(self):
		return [get_df(path) for path in self.path]


class Vector(object):
	"""
	Instantiates and creates a vectorizer, fits it on the data, transforms it and holds all the important info for it.
	"""

	def __init__(self, data, vect_type=CountVectorizer, max_df=0.5, min_df=0.1, n=1):
		self.data, self.vect_type, self.max_df, self.min_df, self.n = data, vect_type, max_df, min_df, n
		self.vect = self.get_vect()
		self.df = self.transform()

	def get_vect(self):
		"""
		Instantiates a vectorizer with RegexpTokenizer and fits it to the given data.

		:return: fitted vectorizer
		:rtype:
		"""
		regexTknzr = RegexpTokenizer(r'\w+')
		vect = self.vect_type(tokenizer=regexTknzr.tokenize, ngram_range=(1, self.n), stop_words='english',
							  max_df=self.max_df,
							  min_df=self.min_df)
		vect.fit(self.data)
		return vect

	def transform(self):
		"""
		Transforms the data using the vectorizer and returns an encoded dataframe.

		:return: Dataframe of encoded features
		:rtype: pandas.Dataframe
		"""
		sparse_df = self.vect.transform(self.data)
		return pd.DataFrame(sparse_df.toarray(), columns=self.vect.get_feature_names())


def parse(path):
	g = gzip.open(path, 'rb')
	for l in g:
		assert isinstance(l, str)
		yield eval(l)


def get_df(path):
	"""

	:rtype: DataFrame
	"""
	i = 0
	df = {}
	for d in parse(path):
		df[i] = d
		i += 1
	return pd.DataFrame.from_dict(df, orient='index')


def rep(s):
	"""
	Converts the parsed key dictionary regex solutions to the corresponding category values

	:param s: Document
	:type s: string
	:return: Processed document
	:rtype: string
	"""
	parse_dict = {
		#     " *_+": " __underscore__",
		" *\d+": " __number__"
	}
	for k, v in parse_dict.items():
		s = re.sub(" *\d+", " #### ", s)
	return s
