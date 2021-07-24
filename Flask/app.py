from flask import Flask, request, jsonify
#from processor.processor import QueryProcessor
# from elastic_search.tfidf import *
from elastic_search.data import Data
from elastic_search.beta_search import beta_search
from flask_cors import CORS, cross_origin

app = Flask(__name__)
#queryprocessor = QueryProcessor()

CORS(app, support_credentials=True)
@app.route("/")
@cross_origin(supports_credentials=True)
def home():
    return "Hello!"

@app.route("/search_beta")
@cross_origin(supports_credentials=True)
def beta():
    query = request.args.get('query')
    #user_question = queryprocessor.generic_preprocessor(query)
    hits=beta_search(query)
    return jsonify({"query": "{}".format(query), "hits": hits})

@app.route("/search")
@cross_origin(supports_credentials=True)
def search():
    query = request.args.get('query')
    user_question = queryprocessor.generic_preprocessor(query)
    
    # faq
   
    # QnA DB
    
    return jsonify({"query": "{}".format(query), "hits": hits})


if __name__ == "__main__":
    app.run(host=" 192.168.1.4", port="8000", debug=True)
