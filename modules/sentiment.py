from textblob import TextBlob
import pandas as pd

class Sentiment(object):

    def get_reviews_sentiment(self,reviews):
        """= 0
        reviews_df['sentiment_type'] = 0
        reviews_df[['sentiment_score',  'sentiment_type']] = reviews_df.apply(self.calculateSentiment,axis=1)

        Calculates Sentiment analysis of all reviews found and return most relevant and diverse reviews
        :param reviews:
        :return:
        """
        reviews_df = pd.DataFrame(reviews)
        reviews_df['sentiment_score']
        return reviews_df.T.to_dict().values()


    def get_answer_sentiment(self,answer):
        """
        Calculates sentiment of the most relevant Answer found
        :param answer:
        :return:
        """
        answer_text = answer['answer']
        sent_score = TextBlob(answer_text).sentiment.polarity
        answer['sentiment_score'] = sent_score
        if(sent_score > 0):
            answer['sentiment_type'] = 'Positive'
        elif (sent_score < 0):
            answer['sentiment_type'] = 'Negative'
        else:
            answer['sentiment_type'] = 'Neutral'
        return answer

    def calculateSentiment(self,review):
        """
        Calculates sentiment of a reviewText and returns Sentiment score and Sentiment Type
        :param review:
        :return:
        """

        review_text = review['reviewText']
        senti_score = TextBlob(review_text).sentiment.polarity
        if (senti_score > 0):
            senti_type = 'Positive'
        elif (senti_score < 0):
            senti_type = 'Negative'
        else:
            senti_type = 'Neutral'
        return pd.Series({'sentiment_score':senti_score,'sentiment_type':senti_type})

    def getDiverseReviews(self,df_sent):
        """
        Returns 3 diverse reviews(Positive, Negative and Neutral) with hightest BM25 scores
        :param df_sent:
        :return:
        """

        df_sent = df_sent.sort_values(by='score', ascending=False)
        pos = df_sent[df_sent.Sent == 'Positive'].iloc[0]
        neg = df_sent[df_sent.Sent == 'Negative'].iloc[0]
        neutral = df_sent[df_sent.Sent == 'Neutral'].iloc[0]
        pos_dic = pos.to_dict()
        neg_dic = neg.to_dict()
        neut_dic = neutral.to_dict()
        return [pos_dic, neg_dic, neut_dic]


