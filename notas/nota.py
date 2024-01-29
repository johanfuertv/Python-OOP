from usuarios.conexion import conectar

connect = conectar()
database =  connect[0]
cursor = connect[1]

class Note:
    def __init__(self, usuario_id, titulo,descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        
    def save(self):
        sql = "INSERT INTO notes VALUES(null, %s, %s, %s, NOW())"
        cursor.execute(sql, (self.usuario_id, self.titulo, self.descripcion))
        database.commit()
        result = [cursor.rowcount, self]
        return result
    
    def list(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        
        cursor.execute(sql)
        result = cursor.fetchall()
        
        return result
    
    def delete(self,titulo):
        sql = "DELETE FROM notas WHERE usuario_id = %s AND titulo = %s"
        cursor.execute(sql, (self.usuario_id, self.titulo))
        database.commit()
        result = [cursor.rowcount, self]
        return result
        