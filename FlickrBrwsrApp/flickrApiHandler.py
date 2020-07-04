import json
import flickrapi
from os import environ

REST_URL = environ.get('REST_URL', 'https://api.flickr.com/services/rest/')
API_KEY = environ.get('API_KEY', 'cdfbcb47c0d9b9040ffd6f7bdb79c750')
SECRET = environ.get('SECRET', 'f45506c76e17d5a8')

class FlickrApiHandler:
    def __init__(self):
        self.flickr = flickrapi.FlickrAPI(API_KEY, SECRET, format='json')

    def getImages(self, per_page = 21, page = 1):
        try:
            res = self.flickr.photos.getRecent(extras='url_q', per_page=per_page, page=page)
        except:
            raise Exception("Failed to fetch recent posts")
        
        photos = []
        try:
            jsonData = json.loads(res)
            for p in jsonData['photos']['photo']:
                photos.append({'id': p['id'],'thumbnail': p['url_q']})
        except:
            raise Exception("Failed to parse response")
        
        return photos

    def getImageInfo(self, photo_id):
        try:
            res = self.flickr.photos.getInfo(photo_id=photo_id)
        except:
            raise Exception("Failed to fetch recent posts")

        try:
            jsonData = json.loads(res)
        except:
            raise Exception("Failed to parse response")

        return jsonData['photo']

    def searchImages(self, searchParams, per_page = 21, page = 1):
        try:
            res = self.flickr.photos.search(text=searchParams, per_page=per_page, page=page, extras='url_q', sort='relevance', privacy_filter=1)
        except:
            raise Exception("Failed to fetch recent posts")
        
        photos = []
        try:
            jsonData = json.loads(res)
            for p in jsonData['photos']['photo']:
                photos.append({'id': p['id'],'thumbnail': p['url_q']})
        except:
            raise Exception("Failed to parse response")
        
        return photos







