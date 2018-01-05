class CONST(object):
    """
    Constant values that raise TypeError when one tries to change them
    """
    COL_SCORE = 'sentiment_score'
    COL_TYPE = 'sentiment_type'
    COL_REVIEW = 'reviewText'
    COL_QUESTION = 'question'
    COL_BM25 = 'bm25_score'
    COL_DELETE = 'delte_flag'
    COL_SIMILAR = 'similarity_score'
    COL_ANSWER = 'answer'

    def __setattr__(self, *_):
        raise TypeError('Cannot change CONST values')

# CONST = CONST()
