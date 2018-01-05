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
            senti_type = Type.POSITIVE
        elif senti_score < 0:
            senti_type = Type.NEGATIVE
        else:
            senti_type = Type.NEUTRAL

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

    # def get_reviews_sentiment(self):
    #     """
    #     Calculates Sentiment analysis of all reviews found and return most relevant and diverse reviews
    #     :param reviews:
    #     :return:
    #     """
    #     reviews_df = self.data
    #     reviews_df['sentiment_score'] = 0
    #     reviews_df['sentiment_type'] = Type.NEUTRAL
    #     key = 'reviewText'
    #     reviews_df[['sentiment_score', 'sentiment_type']] = reviews_df.apply(self.calculate_sentiment, args=([key]),
    #                                                                          axis=1)
    #
    #     top_3_reviews = self.get_diverse_reviews(reviews_df)
    #
    #     return top_3_reviews

    # def get_answers_sentiment(self):
    #     """
    #     Calculates Sentiment analysis of all reviews/asnwers found and return best matched results
    #     :param reviews:
    #     :return:
    #     """
    #     answer_df = self.data
    #     answer_df['sentiment_score'] = 0
    #     answer_df['sentiment_type'] = 0
    #     key = 'answer'
    #     answer_df[['sentiment_score', 'sentiment_type']] = answer_df.apply(self.calculate_sentiment, args=([key]),
    #                                                                        axis=1)
    #
    #     answer_df = answer_df.sort_values(by='bm25_score', ascending=False)
    #
    #     if answer_df.empty:
    #         best_answer = {}
    #     else:
    #         best_answer = answer_df.iloc[0].to_dict()
    #
    #     return best_answer

    # def get_diverse_reviews(self, reviews_data):
    #     """
    #     Returns 3 diverse reviews(Positive, Negative and Neutral) with hightest BM25 scores
    #     :param df_sent:
    #     :return:
    #     """
    #     df_sent = pd.DataFrame(reviews_data)
    #
    #     df_sent = df_sent.sort_values(by='bm25_score', ascending=False)
    #
    #     pos = df_sent[df_sent.sentiment_type == POSITIVE]
    #     neg = df_sent[df_sent.sentiment_type == NEGATIVE]
    #     neutral = df_sent[df_sent.sentiment_type == NEUTRAL]
    #
    #     if pos.empty:
    #         pos_dic = {}
    #     else:
    #         pos_dic = pos.iloc[0].to_dict()
    #
    #     if neg.empty:
    #         neg_dic = {}
    #     else:
    #         neg_dic = neg.iloc[0].to_dict()
    #
    #     if neutral.empty:
    #         neut_dic = {}
    #     else:
    #         neut_dic = neutral.iloc[0].to_dict()
    #
    #     return [pos_dic, neg_dic, neut_dic]
