import sys  # noqa

sys.path.append("..")  # noqa
sys.path.append("....")  # noqa

# from modules.processInput import Input as ProcessInput  # noqa
from modules.bm25 import BM25
from modules.sentiment import Sentiment
from services import queries


def get_most_relevant_question(raw_query, pid):
    """
    Returns set of most relevant questions using Spacy's doc similarity and BM25
    :param raw_query:
    :param pid:
    :return:
    """
    # processed_input = ProcessInput(raw_query)
    data = queries.find_by_asin_with_textscore(pid, raw_query)
    if not data:
        return None

    bm25 = BM25(data, raw_query)
    result = bm25.get_bm25_scores()
    return result


def get_most_relevant_reviews(query, pid):
    """
    Returns set of most relevant reviews using Spacy's doc similarity and BM25
    :param query:
    :param pid:
    :return:
    """
    data = queries.find_reviews_by_asin(pid, query)
    if not data:
        return None

    bm25 = BM25(data, query)
    bm25_reviews = bm25.get_bm25_scores()
    return bm25_reviews


def get_answer_sentiment(question):
    """
    Returns 1 best question along with it's sentiment
    :param question:
    :return:
    """
    s = Sentiment(question)
    sentimented_question = s.get_answers_sentiment()
    return sentimented_question


def get_reviews_sentiment(reviews):
    """
    Returns 3 best reviews along with their diverse sentiment
    :param reviews:
    :return:
    """
    s = Sentiment(reviews)
    sentimented_reviews = s.get_reviews_sentiment()
    return sentimented_reviews
