import pandas as pd
import spacy
from gensim.summarization.bm25 import BM25

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
        self.data = pd.DataFrame(data).fillna(0)
        self.query = unicode(query)  # noqa
        self.column = column
        self.threshold = threshold

    def __fill_similar_docs(self):
        """
        Fills data with similarity scores and filters those documents for the query which have score greater than the
        threshold value
        """
        docs = self.data[self.column].apply(nlp)
        query = nlp(self.query)

        self.data[CONST.COL_SIMILAR] = docs.apply(query.similarity)

        self.data = self.data[self.data[CONST.COL_SIMILAR] > self.threshold]

    def __fill_bm25_scores(self):
        """
        Calculates BM25 scores of each document in corpus for a query
        """
        corpus = [Input(doc).tokens for doc in self.data[self.column]]

        bm25 = BM25(corpus)
        average_idf = sum(float(val) for val in bm25.idf.values()) / float(len(bm25.idf))
        query = Input(self.query).tokens

        scores = bm25.get_scores(query, average_idf)
        self.data[CONST.COL_BM25] = scores

    def get_scored_docs(self):
        """
        Get a list of dictionaries with all the required scores

        :return: list of dictionaries
        :rtype: list of dict
        """
        self.__fill_similar_docs() if self.__data_exists() else None
        self.__fill_bm25_scores() if self.__data_exists() else None
        if self.__data_exists():
            sentiment = Sentiment(self.data, self.column)
            self.data = sentiment.get_sentiment()

        if self.__data_exists() and self.column == CONST.COL_QUESTION:
            return self.data.iloc[0].to_dict()

        return self.data.T.to_dict().values() if self.__data_exists() else None

    def __data_exists(self):
        """
        Returns True if data exists else false.
        :return: Bool value
        :rtype: Bool
        """
        if self.data is None:
            return False
        elif self.data.empty:
            return False
        else:
            return True
