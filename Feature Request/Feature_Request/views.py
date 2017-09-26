"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Feature_Request import application

@application.route('/')
@application.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@application.route('/about')
def about():
     return render_template(
         'about.html',
         title='About',
         year= datetime.now().year,
     )
