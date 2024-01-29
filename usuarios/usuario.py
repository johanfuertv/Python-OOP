import datetime
import hashlib
from usuarios.conexion import conectar

connect = conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.id = None  # El ID se establecerá automáticamente en la base de datos
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))

        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except Exception as e:
            print("Error al registrar usuario:", e)
            result = [0, self]

        return result

    def identificar(self):
        #Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))
        
        #Datos para la consulta
        
        usuario = (self.email,cifrado.hexdigest())
        
        cursor.exceute(sql,usuario)
        result = cursor.fetchone()
        
        cursor.commit()