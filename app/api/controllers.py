from flask import Blueprint
from flask import request, jsonify

import utils

api = Blueprint('api', __name__)


@api.route('/', methods=['POST'])
def find_by_pid():
    request_data = request.get_json()
    raw_query = request_data['query']
    pid = request_data['pid']
    response = {}
    if pid and raw_query:
        scored_question = utils.get_most_relevant_question(raw_query, pid)
        # ToDO: Move the following reviews to a seprate view & fire two requests from front-end
        scored_reviews = utils.get_most_relevant_reviews(raw_query, pid)

        # answer_sentiment = utils.get_answer_sentiment(relevant_question) if relevant_question else None
        # reviews_sentiment = utils.get_reviews_sentiment(relevant_reviews) if relevant_reviews else None

        response['success'] = True
        response['data'] = scored_question
        response['reviews'] = scored_reviews

        if not scored_question:
            response['success'] = False
            response['data'] = None

        if not scored_reviews:
            response['success'] = False
            response['reviews'] = None

    else:
        response['success'] = False
        response['error'] = 'Please enter a valid search query'

    return jsonify(response)
