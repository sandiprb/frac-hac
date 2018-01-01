from textblob import TextBlob
import pandas as pd

POSITIVE = 1
NEGATIVE = -1
NEUTRAL = 0

class Sentiment(object):

    def __init__(self, reviews):
        self.reviews = reviews

    def get_reviews_sentiment(self):
        """
        Calculates Sentiment analysis of all reviews found and return most relevant and diverse reviews
        :param reviews:
        :return:
        """
        reviews_df = pd.DataFrame(self.reviews)
        reviews_df['sentiment_score'] = 0
        reviews_df['sentiment_type'] = 0
        reviews_df[['sentiment_score',  'sentiment_type']] = reviews_df.apply(self.calculate_sentiment, axis=1)

        top_3_reviews = self.get_diverse_reviews(reviews_df)

        return top_3_reviews


    def get_answer_sentiment(self, answer):
        """
        Calculates sentiment of the most relevant Answer found
        :param answer:
        :return:
        """
        answer_text = answer['answer']
        sent_score = TextBlob(answer_text).sentiment.polarity
        answer['sentiment_score'] = sent_score

        if(sent_score > 0):
            answer['sentiment_type'] = POSITIVE
        elif (sent_score < 0):
            answer['sentiment_type'] = NEGATIVE
        else:
            answer['sentiment_type'] = NEUTRAL
        return answer

    def calculate_sentiment(self, review):
        """
        Calculates sentiment of a reviewText and returns Sentiment score and Sentiment Type
        :param review:
        :return:
        """

        review_text = review['reviewText']
        senti_score = TextBlob(review_text).sentiment.polarity
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