"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlickrBrwsrApp import app
from .flickrApiHandler import FlickrApiHandler

@app.route('/')
@app.route('/<page>')
def home_paged(page=1):
    """Renders the index page, the recent list of images by page number"""
    try:
        page_num = int(page)
    except:
        page_num = 1

    photos =  FlickrApiHandler().getImages(21, page_num)
    
    return render_template(
        'imagesList.html',
        photos_list=photos,
        next_page=page_num+1,
        prev_page=(0 if page_num <= 1 else page_num-1),
    )

@app.route('/imageDetails/<id>')
def imageDetails(id):
    """Renders the image detils page."""
    img_info = FlickrApiHandler().getImageInfo(id)
    return render_template(
        'imageDetails.html',
        img_info=img_info
    )

@app.route('/search/<searchParams>/<page>')
def search(searchParams, page):
    """Renders the search result page."""
    try:
        page_num = int(page)
    except:
        page_num = 1

    photos = FlickrApiHandler().searchImages(searchParams, 21, page)

    return render_template(
        'imagesList.html',
        prefix='search/'+searchParams,
        photos_list=photos,
        title='Search Results: ' + searchParams,
        next_page=page_num+1,
        prev_page=(0 if page_num <= 1 else page_num-1),
    )
