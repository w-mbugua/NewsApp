from app import app
from flask import render_template
from .request import get_news, get_sources, get_source_news, get_category_news

#views
@app.route('/')
def index():
    """
    :return: index page and its data
    """
    
    title = 'Home - For Current Global News'
    popular_news = get_news('everything')
    top_headlines = get_news('top-headlines')
    news_sources = get_sources()
    return render_template('index.html', title = title, popular=popular_news, top=top_headlines, sources=news_sources)

@app.route('/<source>')
def per_source(source):
    """
    view function that returns articles for each source
    :param source: news source
    :return: its articles
    """
    source_news = get_source_news(source)
    title = source
    return render_template('source.html', title=title, source=source_news)

@app.route('/category/<category>')
def view_category(category):
    category_news = get_category_news(category)
    title = f"{category} news"
    return render_template('category.html', title = title, news_items = category_news)

