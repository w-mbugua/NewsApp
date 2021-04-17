from app import app
from flask import render_template

#views
@app.route('/')
def index():
    """
    :return: index page and its data
    """
    
    title = 'Home - For Current Global News'
    return render_template('index.html', title = title)