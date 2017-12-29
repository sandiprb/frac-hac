from gensim.summarization.bm25 import BM25, get_bm25_weights
# In[7]:


corpus = [
    ["black", "cat", "white", "cat"],
    ["cat", "outer", "space"],
    ["wag", "dog"]
]
result = get_bm25_weights(corpus)

bm25 = BM25(corpus)
average_idf = sum(float(val) for val in bm25.idf.values()) / len(bm25.idf)

weights = []
for doc in corpus:
    scores = bm25.get_scores(doc, average_idf)
    weights.append(scores)

weights


# In[8]:


result


# In[9]:


average_idf


# In[13]:


len(bm25.idf)

