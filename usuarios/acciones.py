import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print("Ok!! Vamos a registrarte en el sistema...")
        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos?: ")
        email = input("¿Cuál es tu email?: ")
        password = input("Introduce tu contraseña ")
        
        # Crear la instancia de Usuario
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        
        if registro [0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con exito")
        else:
            print(f"No te has registrado correctamente")

    def login(self):
        print("Vale!! Identifícate en el sistema...")
        email = input("¿Cuál es tu email?: ")
        password = input("Introduce tu contraseña ")
        
        usuario = modelo.usuario("", email,password)
        login = usuario.identificar()

        if email == login [3]:
            print(f"Bienvenido {login[1]}, te has registrado en el sistema")
            self.nextActions(login)
        else:
            print("No te has identificado correctamente")
            
    def nextActions(self,usuario):
        print("""Acciones disponibles:
        - Crear notas (crear)
        - Mostar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)
        
        accion = input("Que quieres hacer? ")
        hazEl = notas.acciones.Acciones()

        
        if accion == "crear":
            hazEl.crearNote(usuario)
            print("Vamos a crear una nueva nota...")
            usuario.crearNota()
            
        elif accion == "mostrar":
            hazEl.mostrarNotes(usuario)
            print("Vamos a mostrar tus notas...")
            usuario.mostrarNotas()
            
        elif accion == "eliminar":
            print("Vamos a eliminar una nota...")
            usuario.eliminarNota()
            
        elif accion == "salir":
            print("Hasta pronto")
            exit()
            
        def mostrarNotes(self,usuario):
            print(f"Notes de {usuario[1]} aqui tienes tus notas: ")
            
            nota = modelo.Note(usuario[0])
            nota = nota.list(usuario[0])
            
            for nota in notas:
                print("")
                print(f"Titulo: {nota[2]}")
                print(f"Contenido: {nota[3]}")
                print("")