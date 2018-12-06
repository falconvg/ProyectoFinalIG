import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return render.insert() #renderiza la pagina inser.html
    
    def POST(self):
        formulario = web.input() #almacena los datos del formulario
        nombre = formulario['nombre']  #almacena el email escrito en el input
        escuela = formulario['escuela']  #almacena el email escrito en el input
        promedio = formulario['promedio']  #almacena el email escrito en el input
        email = formulario['email']  #almacena el email escrito en el input
        password = formulario['password'] #almacena el password escrito en el input
        model_datos.insert_datos(nombre,escuela,promedio,email, password) #llama al metodo inser_datos y le pasa los datos guardados
        raise web.seeother('/') #redirecciona al index