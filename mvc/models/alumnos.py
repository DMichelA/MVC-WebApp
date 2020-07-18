import mysql.connector

class Alumnos():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='user_utec', 
                password='Utec.2020',
                host='127.0.0.1',
                port=3306,
                database='utec_db'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)

    def select(self):
        try:
            self.connect()
            query = ("SELECT * from alumnos;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'id_alumno': row[0],
                    'matricula': row[1],
                    'nombre': row[2],
                    'onelastname': row[3],
                    'twolastname': row[4],
                    'edad': row[5],
                    'borndate': row[6],
                    'sex': row[7],
                    'estado': row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

objeto = Alumnos()
objeto.connect()

for row in objeto.select():
    print(row)
