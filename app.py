from flask import Flask, request, jsonify
import pymysql.cursors

app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def get_personas():
    
    personas = [
        {'nombre': 'adrian'},
        {'nombre': 'pedro'},
        {'nombre': 'daniela'},
        {'nombre': 'astrid'},
        {'nombre': 'rafael'},
    ]
 
    return jsonify(personas)

connection = pymysql.Connection(
                                   host='127.0.0.1',
                                   user='root',
                                   password='',
                                   database='leonardo bd',
                                   cursorclass=pymysql.cursors.DictCursor)

     

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
     with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
     return jsonify(usuarios)  

@app.route('/Usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    connection = ()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO Usuario (nombre, edad) VALUES (%s, %s)"
            cursor.execute(sql, (data['nombre'],data['email']))
        connection.commit()
            
    return jsonify({'message': 'creacion exitosa'}), 201

@app.route('/usuarios', methods=['PUT'])
def update_usuario(usuario_id):
    nombre = request.json['nombre']
    email = request.json['email']
    with connection.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s", (nombre, email, usuario_id))
        connection.commit()
    return jsonify({"mensaje": "Usuario actualizado correctamente"})

@app.route('/usuarios', methods=['DELETE'])
def delete_usuario(usuario_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
        connection.commit()
    return jsonify({"mensaje": "Usuario eliminado correctamente"})

if __name__ == '__main__':
    app.run(debug=True)
 
