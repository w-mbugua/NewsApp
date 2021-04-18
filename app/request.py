from app import app
import urllib.request,json
from .models import news, source
import datetime

# Getting api key
api_key = app.config['NEWS_API_KEY']

# getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

News = news.News
Source = source.Source

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
           
            publish_time = publish_time[:10]

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


def process_sources(sources_list):
    """
    function to process the resuts we get from the sources endpoint
    :param sources_list: sources_list, a list of dictionaries containing each source information
    :return: a list of objects
    """
    sources_results = []

    for item in sources_list:
        id = item.get('id')
        name = item.get('name')
        description = item.get('description')
        language = item.get('language')
        source_object = None

        if name and language == 'en':
            source_object = Source(id, name, description)
        sources_results.append(source_object)
    return sources_results


def get_source_news(source):
    # e.g. bbc-news
    get_source_news_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(source,api_key)

    with urllib.request.urlopen(get_source_news_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

    source_articles = None

    if get_source_response['articles']:
        article_list = get_source_response['articles']
        source_articles = process_results(article_list)

    return source_articles


def get_category_news(category):
    get_category_url = 'https://newsapi.org/v2/top-headlines?language=en&category={}&apiKey={}'.format(category, api_key)

    with urllib.request.urlopen(get_category_url) as url:
        category_data = url.read()
        category_response = json.loads(category_data)

    category_news = None
    if category_response['articles']:
        article_list = category_response['articles']
        category_news = process_results(article_list)

    return category_news


def get_covid_news():
    get_covid_news_url = 'https://newsapi.org/v2/top-headlines?q=covid&apiKey={}'.format(api_key)

    with urllib.request.urlopen(get_covid_news_url) as url:
        covid_data = url.read()
        covid_response = json.loads(covid_data)

    covid_articles = None
    if covid_response['articles']:
        covid_articles_list = covid_response['articles']
        covid_articles = process_results(covid_articles_list)

    return covid_articles




