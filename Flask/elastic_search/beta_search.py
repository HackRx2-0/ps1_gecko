from algoliasearch.search_client import SearchClient

import json
import os
APP_ID="4VFSYI5SW0"
API_KEY="b995fc2508fdd096df772d98d72f1f6b"
app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")

client = SearchClient.create(APP_ID, API_KEY)
index = client.init_index('hackrx')
def beta_search(query):

    ans = index.search(query)
    print(ans)

    return ans["hits"]


