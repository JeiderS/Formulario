from flask import Flask , render_template ,request, Response, jsonify, redirect, url_for,flash
import models as dbase
from registro import Registro


db = dbase.dbConnection()
app = Flask(__name__)
app.secret_key = 'hola'

@app.route("/")
def inicio ():
    return render_template("/index.html")


@app.route("/salida")
def salida():
    return render_template("/salida.html")

# metodo para agregar usuario
@app.route("/registros" , methods=["POST"])
def addRegistro ():
    registros = db["registros"]
    Nombre = request.form["Nombre"]
    Usuario = request.form["Usuario"]
    Correo = request.form["Correo"]
    Contraseña = request.form["Contraseña"]
    
    if Nombre and Usuario and Correo and Contraseña:
        registro = Registro( Nombre , Usuario , Correo , Contraseña)
        registros.insert_one(registro.toDBconnection())
        response = jsonify({
            "Nombre":Nombre,
            "Usuario":Usuario,
            "Correo":Correo,
            "Contraseña":Contraseña
        })
        return redirect(url_for('inicio'))
    else:
        return notFound()
    
    
#metodo para autenticar el usuario
@app.route("/Acceso", methods=["POST"])
def login():
    usuarios = db["registros"]
    Usuario = request.form["Usuario"]
    Contraseña = request.form["Contraseña"]

    if Usuario and Contraseña:
        user = usuarios.find_one({"Usuario": Usuario, "Contraseña": Contraseña})
        if user:
            
            return render_template("/salida.html",usuario1=Usuario)
        else:
            flash('Usuario o Contraseña Invalido', 'error')
            return redirect(url_for('inicio'))
    else:
        return notFound()
    
 #metodo para insertar datos en usuario   
@app.route('/preguntas_en/<string:Usuario>', methods=['POST'])
def add_respuesta(Usuario):
    registros = db['registros']
    respuesta1 = request.form['respuesta1']
    respuesta2 = request.form["respuesta2"]
    respuesta3 = request.form["respuesta3"]
    respuesta4 = request.form["respuesta4"]
    respuesta5 = request.form["respuesta5"]
    respuesta6 = request.form["respuesta6"]
    
    if respuesta1:
        usuario_existente = registros.find_one({'Usuario': Usuario})
        if usuario_existente:
            respuestas = usuario_existente.get('Respuestas', [])
            
            respuestas.append(respuesta1)
            respuestas.append(respuesta2)
            respuestas.append(respuesta3)
            respuestas.append(respuesta4)
            respuestas.append(respuesta5)
            respuestas.append(respuesta6)


            registros.update_one({'Usuario': Usuario}, {'$set': {'Respuestas': respuestas}})
            
            response = jsonify({'message': 'Respuesta agregada correctamente'})
            return redirect(url_for('inicio'))
        else:
            return notFound('Usuario no encontrado en la base de datos')
    else:
        return notFound('La respuesta no puede estar vacía')
    
    
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
        }
    response = jsonify(message)
    response.status_code = 404
    return response
    
    
    
    





if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)