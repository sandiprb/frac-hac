import sys  # noqa
sys.path.append("..")  # noqa

from flask import Blueprint
from flask import request, jsonify
from . import utils

api = Blueprint('api', __name__)


@api.route('/')
def find_by_pid():
    raw_query = request.args.get('raw_query')
    relevant_question = utils.get_most_relevant_question(raw_query)
    relevant_reviews = utils.get_most_relevant_reviews(
        relevant_question[0]['question'],
        relevant_question[0]['asin'])
    result = {}
    result['success'] = True
    result['data'] = relevant_question
    result['review'] = relevant_reviews

    if not relevant_question:
        result['success'] = False
        result['data'] = 'No data found!'
        result['review'] = 'No data found!'

    return jsonify(result)
