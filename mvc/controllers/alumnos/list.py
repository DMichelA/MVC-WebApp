import web

import mvc.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/", base="template")

class List():

    def GET(self):
        try:
            result = model_alumnos.select()
            return render.list(result) # renderizando list.html
        except Exception as e:
            return "Error " + str(e.args)

