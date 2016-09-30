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
        # (indent correctly) > if token = self.access_token
        c = pycurl.Curl()
        data = StringIO()
        #c.setopt(c.VERBOSE, True)
        c.setopt(c.URL,
        'https://api.instagram.com/v1/users/%s/media/recent/?access_token=%s' % (user_id, token))
        c.setopt(c.WRITEFUNCTION, data.write)
        c.perform()
        c.close()
        response = json.loads(data.getvalue())
        parsed = {}
        parsed = get_thumbnails(response['data'])
        print parsed
        print 'wah'
        return parsed

def get_thumbnails(r):
    d={}
    for i in range(len(r)):
        rk = r[i]['id']
        rv = {"thumbnail_url": r[i]['images']['thumbnail']['url']}
        d["%s" % rk] = rv
        print d
        print 'yay'
    return d
