from urllib import urlopen, urlencode
import json
import pycurl
from StringIO import StringIO

class User(object):


    def __init__(self, *args, **kwargs):
        self.access_token = "access_token"
        self.username = "username"
        self.user_id = "user_id"
        self.full_name = "full_name"
        self.website = "website"
        self.ppicture_url = "picture_url"

    def set_user_id(username):
        if username = self.username:
            user_id = "self"
        else:
            user_id = user.user_id
        return user_id

    def get_recent(user_id, token)
    #count=None, min_id=None, max_id=None figure
    # out what defaults are
        c = pycurl.Curl()
        data = StringIO()
        c.setopt(c.URL, 'https://api.instagram.com/v1/users/user_id/media/recent/?access_token=token')
        c.setopt(c.WRITEFUNCTION, data.write)
        c.perform()
        c.close()
        response = json.loads(data.getvalue())
        return response
