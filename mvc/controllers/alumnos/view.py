import web

import mvc.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/", base="template")

class View():

    def GET(self, id_alumno):
        try:
            result = model_alumnos.view(id_alumno)[0]
            return render.view(result) # renderizando view.html
        except Exception as e:
            return "Error " + str(e.args)
