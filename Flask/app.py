from flask import Flask, request, jsonify
#from processor.processor import QueryProcessor
# from elastic_search.tfidf import *
from elastic_search.data import Data
from elastic_search.beta_search import beta_search

app = Flask(__name__)
#queryprocessor = QueryProcessor()


@app.route("/")
def home():
    return "Hello!"

@app.route("/search_beta")
def beta():
    query = request.args.get('query')
    #user_question = queryprocessor.generic_preprocessor(query)
    hits=beta_search(query)
    return jsonify({"query": "{}".format(query), "hits": hits})

@app.route("/search")
def search():
    query = request.args.get('query')
    user_question = queryprocessor.generic_preprocessor(query)
    
    # faq
   
    # QnA DB
    
    return jsonify({"query": "{}".format(query), "hits": hits})


if __name__ == "__main__":
    app.run(debug=True)
