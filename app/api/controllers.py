import sys  # noqa
sys.path.append("..")  # noqa

from flask import Blueprint
from flask import request, jsonify

from . import utils

api = Blueprint('api', __name__)


@api.route('/', methods=['POST'])
def find_by_pid():
    request_data = request.get_json()
    raw_query = request_data['query']
    pid = request_data['pid']
    relevant_question = utils.get_most_relevant_question(raw_query, pid)

    # ToDO: Move the following reviews to a seprate view & fire two requests from front-end
    relevant_reviews = utils.get_most_relevant_reviews(raw_query, pid)

    answer_sentiment = utils.get_answer_sentiment(relevant_question)
    reviews_sentiment = utils.get_reviews_sentiment(relevant_reviews)

    result = {}
    result['success'] = True
    result['data'] = answer_sentiment
    result['reviews'] = reviews_sentiment

    if not answer_sentiment:
        result['success'] = False
        result['data'] = 'No data found!'

    if not reviews_sentiment:
        result['reviews'] = 'No data found!'

    return jsonify(result)
