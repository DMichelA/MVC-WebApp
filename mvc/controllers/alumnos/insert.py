import web

import mvc.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/", base="template")

class Insert():

    def GET(self):
        try:
            return render.insert() # renderizando insert.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            user_data = web.input()
            matricula = user_data.matricula
            nombre = user_data.name
            apepat =user_data.onelastname
            apemat = user_data.twolastname
            edad = user_data.edad
            fenac = user_data.borndate
            sexo = user_data.sex
            estado = user_data.state
            model_alumnos.insert(matricula, nombre, apepat, apemat, edad, fenac, sexo, estado)
            web.seeother('/alumnos_list')
        except Exception as e:
            print(e)
            return render.insert()