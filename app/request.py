from app import app
import urllib.request,json
from .models import news

# Getting api key
api_key = app.config['NEWS_API_KEY']

# getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

# 1
def get_news(category):
    """
    function that gets thejson resonse to our url request
    """
    get_news_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

    news_results = None

    if get_news_response['articles']:
        news_list = get_news_response['articles']
        news_results = process_results(news_list)
    return news_results
