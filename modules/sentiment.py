from textblob import TextBlob
import pandas as pd

POSITIVE = 1
NEGATIVE = -1
NEUTRAL = 0


class Sentiment(object):

    def __init__(self, data):
        self.data = data

    def get_reviews_sentiment(self):
        """
        Calculates Sentiment analysis of all reviews found and return most relevant and diverse reviews
        :param reviews:
        :return:
        """
        reviews_df = pd.DataFrame(self.data)
        reviews_df['sentiment_score'] = 0
        reviews_df['sentiment_type'] = 0
        key = 'reviewText'
        reviews_df[['sentiment_score', 'sentiment_type']] = reviews_df.apply(self.calculate_sentiment, args=([key]),
                                                                             axis=1)

        top_3_reviews = self.get_diverse_reviews(reviews_df)

        return top_3_reviews

    def get_answers_sentiment(self):
        """
        Calculates Sentiment analysis of all reviews/asnwers found and return best matched results
        :param reviews:
        :return:
        """
        answer_df = pd.DataFrame(self.data)
        answer_df['sentiment_score'] = 0
        answer_df['sentiment_type'] = 0
        key = 'answer'
        answer_df[['sentiment_score', 'sentiment_type']] = answer_df.apply(self.calculate_sentiment, args=([key]),
                                                                           axis=1)

        answer_df = answer_df.sort_values(by='bm25_score', ascending=False)

        if answer_df.empty:
            best_answer = {}
        else:
            best_answer = answer_df.iloc[0].to_dict()

        return best_answer

    def calculate_sentiment(self, data, key):
        """
        Calculates sentiment of a reviewText and returns Sentiment score and Sentiment Type
        :param data:
        :return:
        """

        data_text = data[key]
        senti_score = TextBlob(data_text).sentiment.polarity
        if (senti_score > 0):
            senti_type = POSITIVE
        elif (senti_score < 0):
            senti_type = NEGATIVE
        else:
            senti_type = NEUTRAL

        return pd.Series({'sentiment_score': senti_score, 'sentiment_type': senti_type})

    def get_diverse_reviews(self, reviews_data):
        """
        Returns 3 diverse reviews(Positive, Negative and Neutral) with hightest BM25 scores
        :param df_sent:
        :return:
        """
        df_sent = pd.DataFrame(reviews_data)

        df_sent = df_sent.sort_values(by='bm25_score', ascending=False)

        pos = df_sent[df_sent.sentiment_type == POSITIVE]
        neg = df_sent[df_sent.sentiment_type == NEGATIVE]
        neutral = df_sent[df_sent.sentiment_type == NEUTRAL]

        if pos.empty:
            pos_dic = {}
        else:
            pos_dic = pos.iloc[0].to_dict()

        if neg.empty:
            neg_dic = {}
        else:
            neg_dic = neg.iloc[0].to_dict()

        if neutral.empty:
            neut_dic = {}
        else:
            neut_dic = neutral.iloc[0].to_dict()

        return [pos_dic, neg_dic, neut_dic]
