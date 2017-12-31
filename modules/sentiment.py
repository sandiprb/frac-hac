from textblob import TextBlob
import pandas as pd

class Sentiment(object):

    def get_reviews_sentiment(self,reviews):
        """
        Calculates Sentiment analysis of all reviews found and return most relevant and diverse reviews
        :param reviews:
        :return:
        """
        reviews_df = pd.DataFrame(reviews)
        reviews_df['sentiment_score'] = 0
        reviews_df['sentiment_type'] = 0
        reviews_df[['sentiment_score','sentiment_type']] = reviews_df.apply(self.calculateSentiment,axis=1)

        return reviews_df

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
        neg_dic = pos.to_dict()
        neut_dic = pos.to_dict()
        return [pos_dic,neg_dic,neut_dic]


ans = {
    "id": "5a43e1d0f1cca02c6f5df44f",
    "questionType" : "yes/no",
    "asin" : "602260074X",
    "answerTime" : "Dec 30, 2014",
    "unixTime" : 1419926400,
    "question" : "is the surface in side the smooth?",
    "answerType" : "Y",
    "answer" : "Yes"
}
data = [{"id" : "5a4749acf1cca0eadf9574fe",
    "reviewerID" : "A3G6XNM240RMWA",
    "asin" : "7806397051",
    "reviewerName" : "Karen",
    "helpful" : [0,4],
    "unixReviewTime" : 1378425600,
    "reviewText" : "Great",
    "overall" : 4.0,
    "reviewTime" : "09 6, 2013",
    "summary" : "great quality"
},
        {"id" : "5a4749acf1cca0eadf9574fe",
    "reviewerID" : "A3G6XNM240RMWAeee",
    "asin" : "7806397051",
    "reviewerName" : "Karen",
    "helpful" : [0,4],
    "unixReviewTime" : 1378425600,
    "reviewText" : "Very Bad",
    "overall" : 4.0,
    "reviewTime" : "09 6, 2013",
    "summary" : "great quality"
},
{"id" : "5a4749acf1cca0eadf9574fe",
    "reviewerID" : "A3G6XNM240RMWA",
    "asin" : "7806397051",
    "reviewerName" : "Karen",
    "helpful" : [0,4],
    "unixReviewTime" : 1378425600,
    "reviewText" : "Yes",
    "overall" : 4.0,
    "reviewTime" : "09 6, 2013",
    "summary" : "great quality"
},

       ]

s = Sentiment()


print s.get_reviews_sentiment(data)
print s.get_answer_sentiment(ans)