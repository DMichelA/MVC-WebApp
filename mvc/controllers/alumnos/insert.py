import web

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
            print(user_data)
            print(user_data.matricula)
            print(user_data.name)
            print(user_data.onelastname)
            print(user_data.twolastname)
            print(user_data.edad)
            print(user_data.borndate)
            print(user_data.sex)
            print(user_data.state)
            return render.insert()
        except Exception as e:
            return "Error" + str(e.args)