from flask import Flask, request, jsonify
from processor.processor import QueryProcessor 
app = Flask(__name__)
queryprocessor=QueryProcessor()

@app.route("/")
def home():
    return "Hello!"

@app.route("/search")
def search():
    query = request.args.get('query')
    ok=queryprocessor.generic_preprocessor(query)
    return jsonify({"message": "{}".format(ok)})

if __name__ == "__main__":
    app.run( debug=True)