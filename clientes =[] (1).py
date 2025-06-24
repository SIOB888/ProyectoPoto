clientes =[]
def registrar_cliente():
    existe = False
    while True:
        try:
            id = int(input("Ingrese ID: "))
        except ValueError:
            print("Ingrese solo números")
        else:
            for cliente in clientes:
                if cliente["id"] == id:
                    print("El ID se encuentra registrado")
                    existe = True
                    break
            if existe == False:
                break
    
    nombre = input("Ingrese nombre: ")

    while True:
        email = input("Ingrese email: ")
        if "@" in email and "." in email:
            break
        else:
            print("El mail debe tener @ y .")
        """
        if email.find("@") != -1 and email.find(".") != -1:
            print("El email debe tener @ y .")
        else:
            break
        """

    cliente = {
        "id":id,
        "nombre":nombre,
        "email":email
    }
    clientes.append(cliente)
    print("Cliente ingresado con exito!!")

def buscar_cliente():
    existe_buscar = False
    while True:
        try:
            id = int(input("Ingrese ID: "))
        except ValueError:
            print("Ingrese solo números")
        else:
            for cliente in clientes:
                if cliente["id"] == id:
                    print(f"----DATOS DEL CLIENTE: {cliente["id"]}\nnombre: {cliente["nombre"]}\nemail: {cliente["email"]}\n")
                    existe_buscar = True
                    break
            
            if existe_buscar == False:
                print("No se encontro el cliente!! ")
            break
            
def listar_clientes():
    if len(clientes) == 0:
        print("No se han registrado clientes")
    else:
        print("-------LISTA DE CLIENTES-------")
        for cliente in clientes:
            print(f"ID: {cliente["id"]}\nnombre: {cliente["nombre"]}\nemail: {cliente["email"]}\n")

def eliminar_cliente():
    existe_buscar = False
    while True:
        try:
            id = int(input("Ingrese ID: "))
        except ValueError:
            print("Ingrese solo números")
        else:
            for cliente in clientes:
                if cliente["id"] == id:
                    clientes.remove(cliente) #validar
                    existe_buscar = True
                    print("Ciente eliminado con exito!!")
                    break
            if existe_buscar == False:
                print("No se encontro el cliente!! ")
            break

def salir():
    print("Saliendo del sistema de gestion de clientes!!")

while True:
    print("""
        ----MENU----
        1- Registrar nuevo cliente
        2- Buscar cliente por ID
        3- Mostrar todos los clientes
        4- Eliminar cliente
        5- Salir
        """)
    try:
        op = int(input("Seleccione una opción: "))
    except ValueError:
        print("Solo ingres números...")
    else:
        match (op):
            case 1:
                registrar_cliente()
            case 2:
                buscar_cliente()
            case 3:
                listar_clientes()
            case 4:
                eliminar_cliente()
            case 5:
                salir()
                break
            case _:
                print("Opción no válida, Ingrese un número de 1 a 5")
                        
            


        