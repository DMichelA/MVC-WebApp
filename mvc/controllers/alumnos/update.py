import web

import mvc.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/", base="template")

class Update():

    def GET(self, id_alumno):
        try:
            result = model_alumnos.view(id_alumno)[0]
            return render.update(result) # renderizando update.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self, id_alumno):
        try:
            form = web.input()
            id_alumno = form.id_alumno
            matricula = form.matricula
            nombre = form.name
            onelastname = form.onelastname
            twolastname = form.twolastname
            edad = form.edad
            borndate = form.borndate
            sex = form.sex
            estado = form.state
            result = model_alumnos.update(id_alumno, matricula, nombre, onelastname, twolastname, edad, borndate, sex, estado)
            web.seeother('/alumnos_list')
        except Exception as e:
            print(e)
            return "Error"