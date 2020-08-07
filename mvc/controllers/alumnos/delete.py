import web

import mvc.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/", base="template")

class Delete():

    def GET(self, id_alumno):
        try:
            result = model_alumnos.view(id_alumno)[0]
            return render.delete(result) # renderizando delete.html
        except Exception as e:
            print(e)
            return "Error"

    def POST(self, id_alumno):
        try:
            form = web.input()
            id_alumno = form.id_alumno #hidden
            result = model_alumnos.delete(id_alumno)
            web.seeother('/alumnos_list')
        except Exception as e:
            print(e)
            return "Error"