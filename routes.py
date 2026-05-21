"""
Routes and views for the bottle application.
"""

from bottle import route, view, static_file
from datetime import datetime

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

@route('/')
@route('/home')
@view('dota')
def home():
    """Renders the home page (Dota)."""
    return dict(
        title='Dota 2 Guide',
        page_style='dota.css', # Передаем имя файла стилей
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About Us',
        page_style='about.css', # Передаем имя файла стилей
        year=datetime.now().year
    )

@route('/deadlock')
@view('deadlock')
def deadlock():
    """Renders the deadlock page."""
    return dict(
        title='Deadlock Guide', 
        page_style='deadlock.css', # Передаем имя файла стилей
        year=datetime.now().year
    )