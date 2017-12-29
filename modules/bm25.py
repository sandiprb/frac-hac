import pandas as pd
import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize
import math


df = pd.read_csv('sample_ques.csv',header=None,index_col=0,names=['question'])
print df.head()


class BM25:

    def __init__(self, corpus):
        self.corpus = corpus
        self.dictionary = corpora.Dictionary()
        self.buildCorpus()
        self.docLen = []
        self.dF = {}
        self.docTF = []
        self.N = 0
        self.docIDF = {}
        self.generateTFIDF()

    def buildCorpus(self):
        raw_data = []
        for value in self.corpus.items():
            data = value['question']
            tokens = word_tokenize(data)
            raw_data.append(tokens)
        self.dictionary.add_documents(raw_data)

    def generateTFIDF(self):
        tot_doc_length = 0
        for data in self.corpus:
            #doc = data
            doc = word_tokenize(data)
            tot_doc_length += len(doc)
            self.docLen.append(len(doc))
            bow = dict([(term, freq*1/float(len(doc)))for term, freq in self.dictionary.doc2bow(doc)])


            for term, tf in bow.items():
                if term not in self.dF:
                    self.dF[term] = 0
                self.dF[term] += 1

            self.docTF.append(bow)
            self.N = self.N + 1

            for term in self.dF:
                self.docIDF[term] = math.log((self.N - self.dF[term] + 0.5) / (self.dF[term] + 0.5))

        self.avgDocLen = tot_doc_length / self.N


    def getBM25Scores(self,query=[],k1=1.5, b=0.75):
        query_bow = self.dictionary.doc2bow(query)
        scores = []
        #for id in self.corpus.keys():
        for indx, doc in enumerate(self.docTF):
            common_terms = set(doc.keys()) & set(dict(query_bow).keys())
            doc_terms_len = self.docLen[indx]
            temp_score = []
            for term in common_terms:
                numertr = (doc[term] * (k1 + 1))
                denomtr = (doc[term] + k1 * (1 - b + b * (doc_terms_len/ self.avgDocLen)))
                temp_score.append(self.docIDF[term] * (numertr) / denomtr)
            scores.append(sum(temp_score))
        return scores

corpus = df.question.values.tolist()
bm = BM25(corpus)

query = 'make up brushes in the trays'
query = word_tokenize(query)
scores = bm.getBM25Scores(query)

print scores
