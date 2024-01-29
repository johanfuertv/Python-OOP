from usuarios import Acciones

hazEl = Acciones(); ##Instanciando mi clase 

print("""  
      Acciones disponibles:
    - registro
    - login
      """)

accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
        
elif accion == "login":
   hazEl.login()