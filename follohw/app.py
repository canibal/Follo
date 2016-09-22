import web
from models.user import User 

urls = (
  '/login', 'Index'
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
        #user_login(username, password)
        return render.index(username = username)

if __name__ == "__main__":
    app.run()
