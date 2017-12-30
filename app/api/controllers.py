import sys
sys.path.append("..")
sys.path.append("....")


from flask import Blueprint
from flask import request, jsonify
from services.queries import find_by_textscore, find_by_asin

from modules.processInput import Input # as ProcessInput


api = Blueprint('api', __name__)


@api.route('/')
def find_by_pid():
    pid = request.args.get('pid')
    raw_query = request.args.get('raw_query')
    query = Input(raw_query, pid)
    # data = find_by_asin(pid)
    print (query.__dict__)
    # return jsonify(data)
    return 'Success'

    # extract PID from raw query
    # PID - >
    # return jsonify(data)

