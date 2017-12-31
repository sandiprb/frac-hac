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
    result = {}
    result['success'] = True
    result['data'] = relevant_question

    if not relevant_question:
        result['success'] = False
        result['data'] = 'No data found!'

    return jsonify(result)
