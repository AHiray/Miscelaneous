import requests 
import json
import re
# get the API KEY here: https://developers.google.com/custom-search/v1/overview
API_KEY = "AIzaSyCqoqkM7rlTVS2bddDrDJCUNXODA1Tt1cQ"
# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = "012795903654895971707:wwsywzknq0t"

# the search query you want
query = input("Job? ")
# constructing the URL
# doc: https://developers.google.com/custom-search/v1/using_rest
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"

# make the API request
data = requests.get(url).json()
print(data)

# get the result items
search_items = data.get("items")
# iterate over 10 results found
for i, search_item in enumerate(search_items, start=1):
    # get the page title
    title = search_item.get("title")
    # page snippet
    snippet = search_item.get("snippet")
    # alternatively, you can get the HTML snippet (bolded keywords)
    html_snippet = search_item.get("htmlSnippet")
    # extract the page url
    link = search_item.get("link")

    
    
    # print the results
    print("="*10, f"Result #{i}", "="*10)
    print("Title:", title)
    print("Description:", snippet)
    
    print("URL:", link, "\n")
