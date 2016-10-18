from urllib import urlopen, urlencode
import json
import pycurl
from StringIO import StringIO

class User(object):


    def __init__(self):
        pass
        #self.access_token = access_token
        #self.username = kwargs.get("username")
        #self.user_id = kwargs.get("user_id")
        #self.full_name = kwargs.get("fullname")
        #self.website = kwargs.get("website")
        #self.ppicture_url = kwargs.get("picture_url")

    def set_user_id(self, username, other_user=None, user_id=None):
        if other_user == None:
            user_id = "self"
            #print "worked"
            return user_id
        else:
            user_id = user_id
            print "didn't work"
            return user_id

    def get_recent(self, user_id, token):
        #count=None, min_id=None, max_id=None figure
        # out what defaults are
        # (indent correctly) > if token = self.access_tokena
        # print user_id
        response = curl_get('https://api.instagram.com/v1/users/%s/media/recent/?access_token=%s' % (user_id, token))
        parsed = {}
        try:
            parsed = get_thumbnails(response['data'])
        except KeyError:
            parsed = "this user is private"
        return parsed

    def get_bio(self, user_id, token):
        response = curl_get('https://api.instagram.com/v1/users/%s/?access_token=%s' % (user_id, token))
        return response['data']['bio']

    def get_follow(self, user_id, which, token):
        response = curl_get('https://api.instagram.com/v1/users/%s/%s?access_token=%s' % (user_id, which, token))
        response = response['data']
        for i in response:
            u_id = i['id']
            # print u_id
            x = self.get_recent(u_id, token)
            i["recent"] = x
        # print response
        # create list out of response (sort)
        # use user_ids through for loop to call set_user_id & get_recent
        # functions above and append to list item
        return response

def get_thumbnails(r):
    dlist = []
    for i in range(len(r)):
        d = {"media_id": r[i]['id'],
             "thumbnail_url": r[i]['images']['thumbnail']['url'],
             "created": r[i]['created_time'],
             "shortcode": r[i]['link'],
             "location": r[i]['location'],
             "caption": r[i]['caption'],
             "likes": r[i]['likes']['count'],
             "user_has_liked": r[i]['user_has_liked'],
             "comments": r[i]['comments']['count'],
             "tags": r[i]['tags'],
             "user": r[i]['user']
            }
        dlist.append(d)
    return dlist

def curl_get(url):
    c = pycurl.Curl()
    datum = StringIO()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, datum.write)
    c.perform()
    c.close()
    return json.loads(datum.getvalue())
