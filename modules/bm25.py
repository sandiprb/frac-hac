from gensim.summarization.bm25 import BM25
from nltk.tokenize import word_tokenize
import pandas as pd


def get_bm25_scores(data, query):
    """
    Calculates BM25 scores of each document in corpus for a query

    :param data:
    :type data: dict
    :param query:
    :type query: str
    :return:
    :rtype: dict
    """
    corpus_df = pd.DataFrame(data.values(), index=data.keys(), columns=['question'])
    corpus = [word_tokenize(qq) for qq in corpus_df.question]
    bm25 = BM25(corpus)
    average_idf = sum(float(val) for val in bm25.idf.values()) / float(len(bm25.idf))
    query = word_tokenize(query)
    scores = bm25.get_scores(query, average_idf)
    corpus_df['scores'] = scores
    return {qid: score for qid, score in zip(corpus_df.index, corpus_df.scores)}
