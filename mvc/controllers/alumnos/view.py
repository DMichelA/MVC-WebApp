import web

render = web.template.render("mvc/views/alumnos/", base="template")

class View():

    def GET(self):
        try:
            return render.view() # renderizando view.html
        except Exception as e:
            return "Error " + str(e.args)
