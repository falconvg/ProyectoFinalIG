import web
'''
Parametros de configuracion para conectarse a una base de datos
MySQL o MariaDB
'''

db_host = 'localhost' 
db_name = 'base_demo'
db_user = 'unid'
db_pw = 'unid.2018'
db_port = 3306

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw,
    port = db_port
    )

'''
Metodo para seleccionar todos los registros de la tabla datos
'''
def select_datos():
    try:
        return db.select('datos')
    except Exception as e:
        print "Model select_datos Error {}".format(e.args)
        print "Model select_datos Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el email dato
'''
def select_email(email):
    try:
        return db.select('datos',where='email=$email', vars=locals())[0]
    except Exception as e:
        print "Model select_email Error {}".format(e.args)
        print "Model select_email Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando email y password 
CREEEEEEEEOOOOOOOOOOOOOOOOOO QUEEEEEEEEEEEEEEE YAAAAAAAAAAAAAAAAAAAAAAAAA
'''
def insert_datos(nombre,escuela,promedio,email,password):
    try:
        return db.insert('datos', nombre=nombre,escuela=escuela,promedio=promedio,email=email,password=password)
    except Exception as e:
        print "Model insert_datos Error {}".format(e.args)
        print "Model insert_datos Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el email dato
'''
def delete_datos(email):
    try:
        return db.delete('datos', where='email=$email',vars=locals())
    except Exception as e:
        print "Model delete_datos Error {}".format(e.args)
        print "Model delete_datos Message {}".format(e.message)
        return None

'''
Metodo para actualizar el email y el password
vamooooosssssssssssssssssssss con estoooooooooooooooooooooooooooooooooooo
'''
def update_datos(nombre,escuela,promedio,email,password):
    try:
        return db.update('datos', 
            nombre=nombre,
            escuela=escuela,
            promedio=promedio,
            email=email,
            password=password, 
            where='email=$email',
            vars=locals())
    except Exception as e:
        print "Model update_datos Error {}".format(e.args)
        print "Model update_datos Message {}".format(e.message)
        return None
