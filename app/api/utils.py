import sys  # noqa
sys.path.append("..")  # noqa
sys.path.append("....")  # noqa


from modules.processInput import Input as ProcessInput
from modules.bm25 import BM25
from modules.sentiment import Sentiment
from services import queries



def get_most_relevant_question(raw_query):
    processed_input = ProcessInput(raw_query)
    product_id = processed_input.product_id[0]
    data = queries.find_by_asin_with_textscore(product_id, raw_query)
    if not data:
        return None

    data = {i['id']: i['question'] for i in data}
    bm25 = BM25(data, raw_query)
    object_id, score = bm25.get_best()
    result = queries.find_by_id(object_id)
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
    print (data)
    data = {i['id']: i['reviewText'] for i in data}
    bm25 = BM25(data, query)
    bm25_reviews = bm25.get_k_best(k=3)
    review_ids = [i[0] for i in bm25_reviews]
    db_fetched_reviews = queries.find_reviews_by_ids(review_ids)
    for i, v in enumerate(db_fetched_reviews):
        for item in bm25_reviews:
            if item[0] == v['id']:
                v['bm25_score'] = item[1]
    return db_fetched_reviews


def get_sentimented_reviews(reviews):
    """
    :param review: list of dict of reviews with bm25 score
    :type review: list of dicts
    :return:
    :rtype:
    """
    s = Sentiment()
    sentimented_reviews = s.get_reviews_sentiment(reviews)
    return sentimented_reviews
