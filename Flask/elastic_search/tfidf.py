from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json
import time
import os
import re
import time
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

# # Cell
# def preprocess(title, body=None):
#     """ Preprocess the input, i.e. lowercase, remove html tags, special character and digits."""
#     text = ''
#     if body is None:
#         text = title
#     else:
#         text = title + body
#     # to lower case
#     text = text.lower()

#     # remove tags
#     text = re.sub("</?.*?>"," <> ", text)

#     # remove special characters and digits
#     text = re.sub("(\\d|\\W)+"," ", text).strip()
#     return text

def create_tfidf_features(corpus, max_features=5000, max_df=0.95, min_df=2):
    """ Creates a tf-idf matrix for the `corpus` using sklearn. """
    tfidf_vectorizor = TfidfVectorizer(decode_error='replace', strip_accents='unicode', analyzer='word',
                                       stop_words='english', ngram_range=(1, 1), max_features=max_features,
                                       norm='l2', use_idf=True, smooth_idf=True, sublinear_tf=True,
                                       max_df=max_df, min_df=min_df)
    X = tfidf_vectorizor.fit_transform(corpus)
    print('tfidf matrix successfully created.')
    return X, tfidf_vectorizor

def calculate_similarity(X, vectorizor, query, top_k=5):
    """ Vectorizes the `query` via `vectorizor` and calculates the cosine similarity of
    the `query` and `X` (all the documents) and returns the `top_k` similar documents."""

    # Vectorize the query to the same length as documents
    query_vec = vectorizor.transform(query)
    # Compute the cosine similarity between query_vec and all the documents
    cosine_similarities = cosine_similarity(X,query_vec).flatten()
    # Sort the similar documents from the most similar to less similar and return the indices
    most_similar_doc_indices = np.argsort(cosine_similarities, axis=0)[:-top_k-1:-1]
    return (most_similar_doc_indices, cosine_similarities)

def show_similar_documents(df, cosine_similarities, similar_doc_indices):
    """ Prints the most similar documents using indices in the `similar_doc_indices` vector."""
    counter = 1
    for index in similar_doc_indices:
        print('Top-{}, Similarity = {}'.format(counter, cosine_similarities[index]))
        print('body: {}, '.format(df[index]))
        print()
        counter += 1

# Cell
def create_index(es_client):
    """ Creates an Elasticsearch index."""
    is_created = False
    # Index settings
    settings = {
        "settings": {
            "number_of_shards": 2,
            "number_of_replicas": 1
        },
        "mappings": {
            "dynamic": "true",
            "_source": {
            "enabled": "true"
            },
            "properties": {
                "body": {
                    "type": "text"
                }
            }
        }
    }
    print('Creating `Question` index...')
    try:
        if es_client.indices.exists(INDEX_NAME):
            es_client.indices.delete(index=INDEX_NAME, ignore=[404])
        es_client.indices.create(index=INDEX_NAME, body=settings)
        is_created = True
        print('index `Question` created successfully.')
    except Exception as ex:
        print(str(ex))
    finally:
        return is_created
    return is_created



def index_data(es_client, data, BATCH_SIZE=100000):
    """ Indexs all the rows in data (python questions)."""
    docs = []
    count = 0
    for line in data:
        js_object = {}
        js_object['body'] = line
        docs.append(js_object)
        count += 1

        if count % BATCH_SIZE == 0:
            index_batch(docs)
            docs = []
            print('Indexed {} documents.'.format(count))
    if docs:
        index_batch(docs)
        print('Indexed {} documents.'.format(count))

    es_client.indices.refresh(index=INDEX_NAME)
    print("Done indexing.")


def index_batch(docs):
    """ Indexes a batch of documents."""
    requests = []
    for i, doc in enumerate(docs):
        request = doc
        request["_op_type"] = "index"
        request["_index"] = INDEX_NAME
        request["body"] = doc['body']
        requests.append(request)
    bulk(es_client, requests)

def run_query_loop():
    """ Asks user to enter a query to search."""
    while True:
        try:
            handle_query()
        except KeyboardInterrupt:
            break
    return


def handle_query(query):
    

    search_start = time.time()
    search = {"size": 3,"query": {"match": {"body": query}}}
    print(search)
    response = es_client.search(index="QUESTIONS", body=json.dumps(search))
    search_time = time.time() - search_start
    print()
    print("{} total hits.".format(response["hits"]["total"]["value"]))
    print("search time: {:.2f} ms".format(search_time * 1000))
    for hit in response["hits"]["hits"]:
        print("id: {}, score: {}".format(hit["_id"], hit["_score"]))
        print(hit["_source"])
        print()
""""
{"mode":"full","isActive":false}

"""