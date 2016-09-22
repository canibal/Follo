import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.login()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        username = "%s" % (form.username)
        return render.index(username = username)

if __name__ == "__main__":
    app.run()
