import web
from follohw import *

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.login()

    def POST(self):
        form = web.input(username="", password="")
        username = "%s" % (form.username)
        password = "%s" % (form.password)
        user_login(username, password)
        return render.index(username = username, access_token = access_token, user_id = user_id, fullname = full_name)

if __name__ == "__main__":
    app.run()
