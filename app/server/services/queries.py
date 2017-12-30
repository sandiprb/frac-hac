from mongo import mongo
from bson import json_util
import json

def find_by_textscore(text):
    cursor = mongo.db.QnA.find(
        {'$text': {'$search': text}},
        {'score': {'$meta': 'textScore'}})

    cursor.sort([('score', {'$meta': 'textScore'})])
    return cursor


def find_by_asin(asin):
    cursor = mongo.db.QnA.find({"asin": asin})
    result = []
    for item in cursor:
        item['id'] = str(item['_id'])
        item.pop('_id')
        result.append(item)

    return result