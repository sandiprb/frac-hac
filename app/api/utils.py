# from modules.processInput import Input as ProcessInput  # noqa
from functools32 import lru_cache

from modules.bm25 import BM25
from modules.getdocuments import Document
from modules.sentiment import Sentiment
from services import queries


@lru_cache()
def get_most_relevant_question(raw_query, pid):
    """
    Returns set of most relevant questions using Spacy's doc similarity and BM25
    :param raw_query:
    :param pid:
    :return:
    """
    # processed_input = ProcessInput(raw_query)
    data = queries.find_by_asin_with_textscore(pid, raw_query)
    if not len(data):
        return None
    doc = Document(data, raw_query, 'question')
    result = doc.get_similar_documents()

    bm25 = BM25(result, raw_query)
    result = bm25.get_bm25_scores()
    return result


@lru_cache()
def get_most_relevant_reviews(query, pid):
    """
    Returns set of most relevant reviews using Spacy's doc similarity and BM25
    :param query:
    :param pid:
    :return:
    """
    data = queries.find_reviews_by_asin(pid, query)
    if not len(data):
        return None
    doc = Document(data, query, 'reviewText')
    result = doc.get_similar_documents()

    bm25 = BM25(result, query)
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
