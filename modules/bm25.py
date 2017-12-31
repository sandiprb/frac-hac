import pandas as pd
from gensim.summarization.bm25 import BM25 as LibBM25
from nltk.tokenize import word_tokenize
from processInput import Input

class BM25(object):
	"""
	Class responsible for Calculating BM25 scores with respect to a query and returning best results
	"""

	def __init__(self, data, query):
		"""

		:param data:
		:param query:
		"""
		self.data = data
		self.query = query
		self.result = self.get_bm25_scores()

	def get_bm25_scores(self):
		"""
		Calculates BM25 scores of each document in corpus for a query

		:param data:
		:type data: dict
		:param query:
		:type query: str
		:return:
		:rtype: dict
		"""
		corpus_df = pd.DataFrame(self.data.values(), index=self.data.keys(), columns=['question'])
		#corpus = [word_tokenize(Input(ques)) for ques in corpus_df.question]
		corpus = []
		for ques in corpus_df.question:
			q = Input(ques)
			corpus.append(q.tokens)
		bm25 = LibBM25(corpus)
		average_idf = sum(float(val) for val in bm25.idf.values()) / float(len(bm25.idf))
		query = word_tokenize(self.query)
		scores = bm25.get_scores(query, average_idf)
		corpus_df['scores'] = scores
		return corpus_df.sort_values(by='scores', ascending=False)

	def get_k_best(self, k=1):
		"""
		Selects 'k' best question.reviews after calculating BM25 scores
		:param dic:
		:param k:
		:return:
		"""
		k_scores = self.result['scores'][:k]
		k_best_vals = zip(k_scores.index, k_scores)
		return k_best_vals

	def get_best(self):
		"""
		Especially made for lazy devs
		:return:
		:rtype: tuple
		"""
		return self.get_k_best(k=1)[0]
