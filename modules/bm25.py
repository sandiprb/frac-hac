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
		# corpus_df = pd.DataFrame(self.data.values(), index=self.data.keys(), columns=['question'])
		corpus_df = pd.DataFrame(self.data)
		corpus = []
		df_key = 'reviewText'

		if 'question' in corpus_df.columns:
			df_key = 'question'

		for ques in corpus_df[df_key]:
			q = Input(ques)
			corpus.append(q.tokens)

		bm25 = LibBM25(corpus)
		average_idf = sum(float(val) for val in bm25.idf.values()) / float(len(bm25.idf))
		query = word_tokenize(self.query)
		scores = bm25.get_scores(query, average_idf)
		corpus_df['bm25_score'] = scores
		return corpus_df.T.to_dict().values()
