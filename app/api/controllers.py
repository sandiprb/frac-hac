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
    relevant_question = utils.get_most_relevant_question(raw_query)
    # ToDO: Move the following reviews to a seprate view & fire two requests from front-end
    relevant_reviews = utils.get_most_relevant_reviews(
        relevant_question[0]['question'],
        relevant_question[0]['asin'])
    sentimented_reviews = utils.get_sentimented_reviews(relevant_reviews)
    result = {}
    result['success'] = True
    result['data'] = relevant_question
    result['reviews'] = sentimented_reviews

    if not relevant_question:
        result['success'] = False
        result['data'] = 'No data found!'
        result['review'] = 'No data found!'

    if not sentimented_reviews:
        result['reviews'] = 'No data found!'

    return jsonify(result)
