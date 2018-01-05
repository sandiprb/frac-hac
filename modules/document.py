import pandas as pd
import spacy
from gensim.summarization.bm25 import BM25
from nltk import word_tokenize

from const import CONST
from modules.processInput import Input
from modules.sentiment import Sentiment

nlp = spacy.load('en')


class Document(object):

    def __init__(self, data, query, column, threshold=0.5):
        """
        Helper methods for semantic similarity of the documents
        :param data:
        :type data:
        :param query:
        :type query:
        :param column:
        :type column:
        """
        self.data = pd.DataFrame(data)
        self.query = unicode(query)  # noqa
        self.column = column
        self.threshold = threshold

    def __fill_similar_docs(self):
        """
        Fills data with similarity scores and returns those documents for the query which have score greater than the
        threshold value

        :return: Request data
        :rtype: dict
        """
        docs = self.data[self.column].apply(nlp)
        query = nlp(self.query)
        self.data[CONST.COL_SIMILAR] = docs.apply(query.similarity)
        similar_data = self.data[self.data[CONST.COL_SIMILAR] > self.threshold]
        return similar_data

    def __fill_bm25_scores(self):
        """
        Calculates BM25 scores of each document in corpus for a query

        :return:
        :rtype: dict
        """
        corpus_df = self.data  # not copying to save on speed. Note that self.data and corpus_df are now references to
        # the same dataframe

        corpus = []
        for ques in corpus_df[self.column]:
            q = Input(ques)
            corpus.append(q.tokens)

        bm25 = BM25(corpus)
        average_idf = sum(float(val) for val in bm25.idf.values()) / float(len(bm25.idf))
        query = word_tokenize(self.query)

        scores = bm25.get_scores(query, average_idf)
        corpus_df[CONST.COL_BM25] = scores

    def __fill_relevant_docs(self):
        """
        Returns the relevant docs dataframe with their bm25 scores
        :return:
        :rtype:
        """
        self.data = self.__fill_similar_docs()
        # __fill_bm25_scores changes self.data already. Statement written only for clarity
        self.data = self.__fill_bm25_scores()
        return self.data

    def get_scored_docs(self):
        """

        :return:
        :rtype:
        """
        sentiment = Sentiment(self.data, self.column)
        self.data = sentiment.get_sentiment()
        return self.data.T.to_dict().values()
