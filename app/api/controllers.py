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
    response = {}
    if pid and raw_query:
        relevant_question = utils.get_most_relevant_question(raw_query, pid)
        # ToDO: Move the following reviews to a seprate view & fire two requests from front-end
        relevant_reviews = utils.get_most_relevant_reviews(raw_query, pid)

        question_setiment = utils.get_question_setiment(relevant_question)
        reviews_sentiment = utils.get_reviews_sentiment(relevant_reviews)

        response['success'] = True
        response['data'] = question_setiment
        response['reviews'] = reviews_sentiment

        if not question_setiment:
            response['success'] = False
            response['data'] = 'No data found!'

        if not reviews_sentiment:
            response['reviews'] = 'No data found!'
    else:
        response['success'] = False
        response['error'] = 'Please enter a valid search query'

    return jsonify(response)
