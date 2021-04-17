from app import app
import urllib.request,json
from .models import news

# Getting api key
api_key = app.config['NEWS_API_KEY']

# getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

News = news.News
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


def process_results(news_list):
    """
    function that processes news results into a list of objects
    :param news_list: a list of dictionaries that contain each article details
    :return: a list of news objects
    """
    news_results = []

    for news_item in news_list:
        title = news_item.get('title')
        author = news_item.get('author')
        description = news_item.get('description')
        link = news_item.get('url')
        image = news_item.get('urlToImage')
        publish_time = news_item.get('publishedAt')

        if image:
            news_object = News(title, author,description, link, image, publish_time)
            news_results.append(news_object)
    return news_results


def get_sources():
    get_sources_url = 'https://newsapi.org/v2/sources?apiKey={}'.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_list = get_sources_response['sources']
            sources_results = process_sources(sources_list)
    return sources_results



