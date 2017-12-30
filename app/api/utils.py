import sys  # noqa
sys.path.append("..")  # noqa
sys.path.append("....")  # noqa


from modules.processInput import Input as ProcessInput
from modules.bm25 import BM25
from services import queries


def get_most_relevant_question(raw_query):
    processed_input = ProcessInput(raw_query)
    product_id = processed_input.product_id[0]
    data = queries.find_by_asin_with_textscore(product_id, raw_query)
    if not data:
        return None

    data = {i['id']: i['question'] for i in data}
    bm25 = BM25(data, raw_query)
    object_id, score = bm25.get_best()
    result = queries.find_by_id(object_id)
    return result