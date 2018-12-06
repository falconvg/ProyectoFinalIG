import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Update:
    def __init__(self):
        pass

    def GET(self, email): 
        datos = model_datos.select_email(email) 
        return render.update(datos)
    
    def POST(self, email):
        formulario = web.input()
        nombre = formulario['nombre']  #almacena el email escrito en el input
        escuela = formulario['escuela']  #almacena el email escrito en el input
        promedio = formulario['promedio']  #almacena el email escrito en el input
        email = formulario['email']  #almacena el email escrito en el input
        password = formulario['password'] #almacena el password escrito en el input
        model_datos.update_datos(nombre,escuela,promedio,email, password) #llama al metodo inser_datos y le pasa los datos guardados
        raise web.seeother('/')
