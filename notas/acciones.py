from notas.nota import Note,save
from notas.acciones import nextActions
class Acciones:
    
    def crearNote(self,usuario):
        print("Vamos a crear una nueva nota...")
        
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")
        
        note = Note(usuario[0],titulo,descripcion)
        guardar = note.save()
        
        if guardar[0] >= 1:
            print(f"Perfecto has guardado la nota: {note.titulo}")
        else:
            print(f"No se ha guardado la nota {usuario[1]}")
        
    def mostrarNotes(self,usuario):
        print("Vamos a mostrar tus notas...")
        
    def deleteNote(self,usuario):
        print("Vamos a eliminar una nota...")