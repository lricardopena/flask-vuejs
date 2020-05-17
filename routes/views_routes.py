from flask import Blueprint, render_template

views_pages = Blueprint('views_pages', __name__)


@views_pages.route('/')
def index():
    return render_template('home/index.html')


@views_pages.route('/about')
def about():
    return render_template('home/about.html')


@views_pages.route('/contact')
def contact():
    return render_template('home/contact.html')