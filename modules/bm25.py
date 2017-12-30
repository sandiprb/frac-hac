from gensim.summarization.bm25 import BM25 as LibBM25
from nltk.tokenize import word_tokenize
import pandas as pd
import operator

class BM25(object):
    """
    Class responsible for Calculating BM25 scores with respect to a query and returning best results
    """

    def __init__(self,data,query):
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
        corpus = [word_tokenize(ques) for ques in corpus_df.question]
        bm25 = LibBM25(corpus)
        average_idf = sum(float(val) for val in bm25.idf.values()) / float(len(bm25.idf))
        query = word_tokenize(self.query)
        scores = bm25.get_scores(query, average_idf)
        corpus_df['scores'] = scores
        dic = {qid: score for qid, score in zip(corpus_df.index, corpus_df.scores)}
        sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
        return sorted_dic

    def getKBest(self, dic, k=1):
        """
        Selects 'k' best question.reviews after calculating BM25 scores
        :param dic:
        :param k:
        :return:
        """
        k_best_vals = {key: dic[key] for key in dic.keys()[:k]}
        return k_best_vals



