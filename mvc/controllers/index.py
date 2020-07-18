import web

render = web.template.render("mvc/views/", base="template")

class Index():

    def GET(self):
        try:
            return render.index() # renderizando index.html
        except Exception as e:
            return "Error " + str(e.args)
