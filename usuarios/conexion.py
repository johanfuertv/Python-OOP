import mysql.connector

def conectar():
    database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python",
    port=3306
    )

    # Cursor para hacer registros en la base de datos
    cursor = database.cursor(buffered=True)

    return [database,cursor]
