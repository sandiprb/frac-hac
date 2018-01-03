import pandas as pd
import spacy


class Document(object):

    def __init__(self, data, query, column):
        """
        Helper methods for semantic similarity of the documents
        :param data:
        :type data:
        :param query:
        :type query:
        :param column:
        :type column:
        """
        self.data = pd.DataFrame(data)
        self.query = unicode(query)  # noqa
        self.column = column
        # self.documents = self.get_documents()

    def __get_documents(self):
        """
        Fetches all the documents returned by DB for a PID
        And creates a dict of key(id) and value(question)
        :return:
        """
        data = {}
        documents = self.data
        for line in documents:
            doc_id = line['id']
            question = line['question']
            data[doc_id] = question
        return data

    def get_similar_documents(self, threshold=0.5):
        """
        Returns similar documents for the query with similarity score greater than the threshold value

        :param threshold: Threshold value
        :type threshold: float
        :return: Request data
        :rtype: dict
        """
        nlp = spacy.load('en')
        docs = self.data[self.column].apply(nlp)
        query = nlp(self.query)
        self.data['similarity_score'] = docs.apply(query.similarity)
        similar_data = self.data[self.data['similarity_score'] > threshold]
        return similar_data.T.to_dict().values()
