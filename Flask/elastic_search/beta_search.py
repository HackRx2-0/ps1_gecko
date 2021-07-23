from algoliasearch.search_client import SearchClient

import json
import os
app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")

client = SearchClient.create(app_id, api_key)
index = client.init_index('hackrx')
def beta_search(query):

    ans = index.search(query)
    print(ans)

    return ans["hits"]


