import pandas as pd
from textblob import TextBlob

from const import CONST
from type import SentimentType as Type


class Sentiment(object):

    def __init__(self, data, column):
        self.data = data
        self.column = column

    def get_sentiment(self):
        """
        Sorts on the basis of BM25 score of the documents. Adds column for sentiment columns. For reviews it also adds
        only top 3 diversified ones.
        :return:
        :rtype:
        """
        self.data[CONST.COL_SCORE], self.data[CONST.COL_TYPE] = 0, 0
        self.data[[CONST.COL_SCORE, CONST.COL_TYPE]] = self.data.apply(self.__get_type, axis=1)
        self.data.sort_values(by=CONST.COL_BM25, ascending=False)
        if self.column == CONST.COL_REVIEW:
            self.data = self.get_diverse_reviews()

        return self.data

    def __get_type(self, data):
        """
        Calculates sentiment of a reviewText and returns Sentiment score and Sentiment Type
        :param data: Series
        :return:
        """
        if self.column == CONST.COL_QUESTION:
            doc = data[CONST.COL_ANSWER]
        else:
            doc = data[CONST.COL_REVIEW]

        senti_score = TextBlob(doc).sentiment.polarity

        if senti_score > 0:
            senti_type = Type.POSITIVE.value
        elif senti_score < 0:
            senti_type = Type.NEGATIVE.value
        else:
            senti_type = Type.NEUTRAL.value

        return pd.Series({CONST.COL_SCORE: senti_score, CONST.COL_TYPE: senti_type})

    def get_diverse_reviews(self):
        """
        Returns 3 diverse reviews(Positive, Negative or Neutral)
        :return:
        :rtype:
        """
        self.data[CONST.COL_DELETE] = False
        i, row_types = 1, [self.data[CONST.COL_TYPE][0]]

        while i > 3:
            col_type = self.data.iloc[i][CONST.COL_TYPE]
            if col_type not in row_types:
                self.data[CONST.COL_DELETE] = True
                row_types.append(col_type)
            i += 1

        self.data = self.data[self.data[CONST.COL_DELETE] == False][:3]
        self.data = self.data.drop(CONST.COL_DELETE, axis=1)

        return self.data
