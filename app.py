from tkinter.tix import AUTO
from flask import Flask ,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://sql10503639:7siUgtepyF@sql10.freesqldatabase.com/sql10503639'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Producto(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(500))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    desc = db.Column(db.String(500))
    imgurl = db.Column(db.String(200))
    def __init__(self,nombre,precio,stock,desc,imgurl):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.desc = desc
        self.imgurl = imgurl
    
db.create_all() #Crea las tablas

class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','stock','desc','imgurl')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many = True)

@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos = Producto.query.all()
    result = productos_schema.dump(all_productos)
    return jsonify(result)

@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    return producto_schema.jsonify(producto)

@app.route('/producto/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)

@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    precio=request.json['precio']
    stock=request.json['stock']
    desc=request.json['desc']
    imgurl=request.json['imgurl']
    new_producto=Producto(nombre,precio,stock,desc,imgurl)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)

@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Producto.query.get(id)
   
    nombre=request.json['nombre']
    precio=request.json['precio']
    stock=request.json['stock']
    desc=request.json['desc']
    imgurl=request.json['imgurl']
 
    producto.nombre=nombre
    producto.precio=precio
    producto.stock=stock
    producto.desc=desc
    producto.imgurl=imgurl
    db.session.commit()
    return producto_schema.jsonify(producto)

if __name__=='__main__':
    app.run(debug=True, port=5000)  