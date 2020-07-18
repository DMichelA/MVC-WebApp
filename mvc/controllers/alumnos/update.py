import web

render = web.template.render("mvc/views/alumnos/", base="template")

class Update():

    def GET(self):
        try:
            return render.update() # renderizando update.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            udata = web.input()
            print(udata)
            print(udata.matricula)
            print(udata.name)
            print(udata.onelastname)
            print(udata.twolastname)
            print(udata.edad)
            print(udata.borndate)
            print(udata.sex)
            print(udata.state)
            return render.update()
        except Exception as e:
            return "Error" + str(e.args)