import pytest

from modules.bm25 import BM25
from modules.getdocuments import Document
from sentiment import Sentiment


class TestClass(object):

    @pytest.mark.skip(reason="test_bm25: test for the old class structure")
    def test_bm25(self):
        dic = {
            '0': 'can you fit make up brushes in the trays',
            '1': 'Can you move all the dividers?',
            '2': 'is the surface in side the smooth?',
            '3': 'How deep do the extending trays measure?',
            '4': 'Can bottles of nail polish stand upright in the top trays when the case is closed?'
        }
        scores = [0, 1.6122192915464926, 0.16122192915464922, 0, 0.16122192915464922]

        bm25 = BM25(dic, dic['0'])
        assert set(bm25.result.scores.tolist()) == set(scores)

    def test_bm25_new(self):
        data = [
            {
                u'questionType': u'yes/no',
                u'asin': u'B00028OSI0',
                u'answerTime': u'Mar 10, 2014',
                u'unixTime': 1394434800,
                u'question': u'can I use this on my face?',
                u'score': 2.0,
                u'answerType': u'?',
                u'answer': u'All over! Buy it its worth every penny.',
                'id': '5a43e1d1f1cca02c6f5dfc0e'
            },
            {
                u'questionType': u'open-ended',
                u'asin': u'B00028OSI0',
                u'answerTime': u'Feb 10, 2015',
                u'unixTime': 1423555200,
                u'question': u'How do I use skin gel for gums and teeth?',
                u'score': 0.6,
                u'answer': u"I don't know; I have never used this product for gums or teeth. Some Aloe can be used/taken internally. However, I would think this product is only for external use. It's really great for your skin. Good luck!",
                'id': '5a43e1d6f1cca02c6f5e1fbe'
            }
        ]

        scores = [0, 1.6122192915464926, 0.16122192915464922, 0, 0.16122192915464922]
        query = 'All over! Buy it its worth every penny.'
        bm25 = BM25(data, query)
        dic = bm25.get_bm25_scores()
        assert 1

    def test_document(self):
        data = [
            {
                u'questionType': u'yes/no',
                u'asin': u'B00028OSI0',
                u'answerTime': u'Mar 10, 2014',
                u'unixTime': 1394434800,
                u'question': u'can I use this on my face?',
                u'score': 2.0,
                u'answerType': u'?',
                u'answer': u'All over! Buy it its worth every penny.',
                'id': '5a43e1d1f1cca02c6f5dfc0e'
            },
            {
                u'questionType': u'open-ended',
                u'asin': u'B00028OSI0',
                u'answerTime': u'Feb 10, 2015',
                u'unixTime': 1423555200,
                u'question': u'How do I use skin gel for gums and teeth?',
                u'score': 0.6,
                u'answer': u"I don't know; I have never used this product for gums or teeth. Some Aloe can be used/taken internally. However, I would think this product is only for external use. It's really great for your skin. Good luck!",
                'id': '5a43e1d6f1cca02c6f5e1fbe'
            }
        ]

        scores = [0, 1.6122192915464926, 0.16122192915464922, 0, 0.16122192915464922]
        query = 'All over! Buy it its worth every penny.'
        doc = Document(data, query, 'question')
        dic = doc.get_similar_documents()
        # print dic
        assert 1

    @pytest.mark.skip(reason="test_sentiment: still left to implement fully")
    def test_sentiment(self):
        ans = {
            "id": "5a43e1d0f1cca02c6f5df44f",
            "questionType": "yes/no",
            "asin": "602260074X",
            "answerTime": "Dec 30, 2014",
            "unixTime": 1419926400,
            "question": "is the surface in side the smooth?",
            "answerType": "Y",
            "answer": "Yes"
        }
        data = [{"id": "5a4749acf1cca0eadf9574fe",
                 "reviewerID": "A3G6XNM240RMWA",
                 "asin": "7806397051",
                 "reviewerName": "Karen",
                 "helpful": [0, 4],
                 "unixReviewTime": 1378425600,
                 "reviewText": "Great",
                 "overall": 4.0,
                 "reviewTime": "09 6, 2013",
                 "summary": "great quality"
                 },
                {"id": "5a4749acf1cca0eadf9574fe",
                 "reviewerID": "A3G6XNM240RMWAeee",
                 "asin": "7806397051",
                 "reviewerName": "Karen",
                 "helpful": [0, 4],
                 "unixReviewTime": 1378425600,
                 "reviewText": "Very Bad",
                 "overall": 4.0,
                 "reviewTime": "09 6, 2013",
                 "summary": "great quality"
                 },
                {"id": "5a4749acf1cca0eadf9574fe",
                 "reviewerID": "A3G6XNM240RMWA",
                 "asin": "7806397051",
                 "reviewerName": "Karen",
                 "helpful": [0, 4],
                 "unixReviewTime": 1378425600,
                 "reviewText": "Yes",
                 "overall": 4.0,
                 "reviewTime": "09 6, 2013",
                 "summary": "great quality"
                 },

                ]

        s = Sentiment()
        actual_review_sentiment = [
            {'reviewerID': 'A3G6XNM240RMWA', 'asin': '7806397051', 'summary': 'great quality', 'reviewerName': 'Karen',
             'helpful': [0, 4], 'unixReviewTime': 1378425600, 'reviewText': 'Great', 'overall': 4.0,
             'id': '5a4749acf1cca0eadf9574fe', 'reviewTime': '09 6, 2013'},
            {'reviewerID': 'A3G6XNM240RMWAeee', 'asin': '7806397051', 'summary': 'great quality',
             'reviewerName': 'Karen',
             'helpful': [0, 4], 'unixReviewTime': 1378425600, 'reviewText': 'Very Bad', 'overall': 4.0,
             'id': '5a4749acf1cca0eadf9574fe', 'reviewTime': '09 6, 2013'},
            {'reviewerID': 'A3G6XNM240RMWA', 'asin': '7806397051', 'summary': 'great quality', 'reviewerName': 'Karen',
             'helpful': [0, 4], 'unixReviewTime': 1378425600, 'reviewText': 'Yes', 'overall': 4.0,
             'id': '5a4749acf1cca0eadf9574fe', 'reviewTime': '09 6, 2013'}]
        actual_ans_sentiment = {'questionType': 'yes/no', 'asin': '602260074X', 'answerTime': 'Dec 30, 2014',
                                'answerType': 'Y', 'sentiment_type': 'Neutral', 'sentiment_score': 0.0, 'answer': 'Yes',
                                'unixTime': 1419926400, 'question': 'is the surface in side the smooth?',
                                'id': '5a43e1d0f1cca02c6f5df44f'}

        review_sentiment = s.get_reviews_sentiment(data)
        answer_sentiment = s.get_answer_sentiment(ans)
        # TODO: write proper assert statement
        assert 1
