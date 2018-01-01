import sys  # noqa

sys.path.append("..")  # noqa
sys.path.append("....")  # noqa

# from modules.processInput import Input as ProcessInput  # noqa
from modules.bm25 import BM25
from modules.sentiment import Sentiment
from services import queries


def get_most_relevant_question(raw_query, pid):
    # processed_input = ProcessInput(raw_query)
    data = queries.find_by_asin_with_textscore(pid, raw_query)
    if not data:
        return None

    bm25 = BM25(data, raw_query)
    result = bm25.get_bm25_scores()
    return result


def get_most_relevant_reviews(query, pid):
    """
    :param query: raw query
    :type query: basestring
    :param pid: pid of selected rew query
    :type pid: basestring
    :return: returns reviews found from db
    :rtype: list of dicts
    """
    data = queries.find_reviews_by_asin(pid, query)
    if not data:
        return None

    bm25 = BM25(data, query)
    bm25_reviews = bm25.get_bm25_scores()
    return bm25_reviews


def get_question_setiment(question):
    """
    :param review: list of dict of questions with bm25 score
    :type review: list of dicts
    :return:
    :rtype:
    """
    s = Sentiment(question)
    sentimented_question = s.get_answers_sentiment()
    return sentimented_question


def get_reviews_sentiment(reviews):
    """
    :param review: list of dict of reviews with bm25 score
    :type review: list of dicts
    :return:
    :rtype:
    """
    s = Sentiment(reviews)
    sentimented_reviews = s.get_reviews_sentiment()
    return sentimented_reviews
