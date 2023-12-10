from flask import Flask ,jsonify ,request 
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend


# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/crud'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow


# defino las tablas
class Empleado(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    apellido=db.Column(db.String(100))
    email=db.Column(db.String(100))
    imagen=db.Column(db.String(400))
    def __init__(self,nombre,apellido,email,imagen):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.apellido=apellido
        self.email=email
        self.imagen=imagen

    #  si hay que crear mas tablas , se hace aqui


with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
class EmpleadoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','apellido','email','imagen')


empleado_schema=EmpleadoSchema()            # El objeto producto_schema es para traer un producto
empleados_schema=EmpleadoSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto


# crea los endpoint o rutas (json)
@app.route('/empleados',methods=['GET'])
def get_Empleados():
    all_empleados=Empleado.query.all()         # el metodo query.all() lo hereda de db.Model
    result=empleados_schema.dump(all_empleados)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla




@app.route('/empleados/<id>',methods=['GET'])
def get_empleado(id):
    empleado=Empleado.query.get(id)
    return empleado_schema.jsonify(empleado)   # retorna el JSON de un producto recibido como parametro


@app.route('/empleados/<id>',methods=['DELETE'])
def delete_empleado(id):
    empleado=Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()                     # confirma el delete
    return empleado_schema.jsonify(empleado) # me devuelve un json con el registro eliminado


@app.route('/empleados', methods=['POST']) # crea ruta o endpoint
def create_empleado():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    apellido=request.json['apellido']
    email=request.json['email']
    imagen=request.json['imagen']
    new_empleado=Empleado(nombre,apellido,email,imagen)
    db.session.add(new_empleado)
    db.session.commit() # confirma el alta
    return empleado_schema.jsonify(new_empleado)


@app.route('/empleados/<id>', methods=['PUT'])
def update_empleado(id):
    empleado=Empleado.query.get(id)
 
    empleado.nombre=request.json['nombre']
    empleado.apellido=request.json['apellido']
    empleado.email=request.json['email']
    empleado.imagen=request.json['imagen']


    db.session.commit()    # confirma el cambio
    return empleado_schema.jsonify(empleado)    # y retorna un json con el producto
 
@app.route('/', methods=['GET'])
def bienvenida():
    return "Bienvenidos a Flask"

# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000