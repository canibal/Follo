import web
from models.user import User
import pycurl
from urllib import urlencode
from StringIO import StringIO
import json
import pprint

urls = (
  '/login', 'Index' 
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
<<<<<<< Updated upstream
        form = web.input(access_token=None)
        access_token = "%s" % form.access_token

        if access_token:
            return render.index(access_token = access_token)
        else:
=======

        try:
            code = web.input()
            code = code.code
            u_name = auth_curl(code)a
            access_token = u_name['access_token']
            username = u_name['user']['username']
            fullname = u_name['user'] 
            return render.index(username = u_name['user']['username'])
        except AttributeError: 
>>>>>>> Stashed changes
            return render.login()

    def POST(self):
        form = web.input(username="")
        username = "%s" % (form.username)
        #user_login(username)
        return render.index(username = username)

def auth_curl(code):
    c = pycurl.Curl()
    data = StringIO()
    c.setopt(c.URL, 'https://api.instagram.com/oauth/access_token')
    oauth_post = {'client_id': '2eed6a9a7b5c4a79bc0cbbc02fe91c22',
                  'client_secret': 'dcfffaaf3ca84ce0bf1508b881c2e634',
                  'grant_type': 'authorization_code',
                  'redirect_uri': 'http://localhost:8080/login',
                  'code': code
                         }
    authposts = urlencode(oauth_post)
    c.setopt(c.POSTFIELDS, authposts)
    c.setopt(c.WRITEFUNCTION, data.write)
    
    c.perform()
    c.close()
    response = json.loads(data.getvalue())
    return response

         #should eventually add response to DB as well/instead


if __name__ == "__main__":
    app.run()
