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
    result = {}
    result['success'] = True
    result['data'] = relevant_question

    if not relevant_question:
        result['success'] = False
        result['data'] = 'No data found!'

    return jsonify(result)
