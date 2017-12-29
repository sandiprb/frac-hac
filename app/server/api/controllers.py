import sys
sys.path.append("..")

from flask import Blueprint
from flask import request, jsonify
from services.queries import find_by_textscore, find_by_asin


api = Blueprint('api', __name__)


@api.route('/')
def index():
    return "APIS end Points"


@api.route('/asin/<pid>')
def find_by_pid(pid):
    data = find_by_asin(pid)
    return jsonify(data)
    # return jsonify(data)

