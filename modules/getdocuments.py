import operator

class Document(object):

    def __init__(self, data):
        """

        :param data:
        """
        self.data = data
        self.documents = self.getDocuments()

    def getDocuments(self):
        """

        :return:
        """
        data = {}
        documents = self.data
        for line in documents:
            doc_id = line['id']
            question = line['question']
            data[doc_id] = question
        return data

    def sortDictionary(self,dict):
        """

        :param dict:
        :return:
        """
        sorted_dic = sorted(dict.items(), key=operator.itemgetter(1))
        return sorted_dic


