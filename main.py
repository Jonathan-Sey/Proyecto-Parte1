
import json
#creacion de base de datos 
try:
    with open("base_de_datos.json","r") as archivo_db:
        print("Carcando base de datos")
        lista_estudiantes = json.load(archivo_db)
        print("base de datos cargada")
except:
    print("Creando base de datos")
    # lista estudiantes
    lista_estudiantes = [] 
     
#calculo del promedio del estudiante 
def promedioNotas(promedio_notas_del_usuario):
    suma = 0
    for nota in promedio_notas_del_usuario:
        suma = (suma + nota)
    lista_notas = len(promedio_notas_del_usuario)
    promedio = suma / lista_notas
    return promedio

# cursos total del estudiante 
def cursos_estudiante (cantidad_cursos):
    total_cursos = len(cantidad_cursos)
    return total_cursos

    # OPCION (1): ingreso de usuario    
def ingreso_de_usuario():
    print("----------INGRESE LOS DATOS DEL ESTUDIANTE----------")
    nombre = input("- Nombre Completo: ")
    carnet = input("- No. Carnet: ")
        
    # Ingreso de las notas del usuario
    # lista que almacena las notas del estudiante 
    notas_del_usuario = []
    # lista de los cursos aprobados
    nota_aprobada = []  
    respuesta_usuario = input("Quiere agregar una nota? (s/n)")
    while   respuesta_usuario == 's' or respuesta_usuario == 'S':
            nota_estudiante =input("Ingrese Nota: ")
            nota_estudiante = int(nota_estudiante)
            notas_del_usuario.append(nota_estudiante)
            if nota_estudiante >= 61:
                nota_aprobada.append(nota_estudiante)
                curso_ganado = len(nota_aprobada)
            respuesta_usuario = input("Quiere agregar otra nota? (s/n)")
            
    # numero de notas del estudiante 
    cursos = cursos_estudiante(notas_del_usuario)
    # promedio estudiante 
    promedio = promedioNotas(notas_del_usuario)

    # año de ingreso 
    año = input("Año: ")
    carnetUsuario = año + "-" + carnet
    # Diccionario de Estudiantes    
    Usuario = {
        'Nombre':nombre,
        'Carnet':carnetUsuario,
        'notas': notas_del_usuario,
        'promedio': promedio,
        'año': año,
        'cursos': cursos,
        'aprobado': curso_ganado      
        
    }     
    #agregando los datos del usuario a la lista de estudiantes
    lista_estudiantes.append(Usuario)
    return

#OPCION (3): Mostrar Lista de Usuarios
def mostrar_lista_de_Usuarios():    
    print(lista_estudiantes)   
    return 


#Creacion de menu.
def funcion_menu():
    texto_menu ="""--------------M E N U -------------
    1. Ingresar un usuario.
    2. Buscar un usuario.
    3. Mostrar el listado de usuarios.
    4. Salir.
    -----------------------
    Elija una opcion 
    """
    op = input(texto_menu)
    op = int(op)
    if op == 1:
        #Ingreso de informacion de un Usuario
        ingreso_de_usuario()
        
    if op == 2:
        # Buscar la informacion de un usuario 
        print("no completado")
        pass

    if op == 3:
        # Mostrar el listado de usuarios disponibles
        mostrar_lista_de_Usuarios()
        
    if op == 4:
        # menu de guardado
        texto_salir = """
        1. Guardar y salir
        2. salir sin guardar 
        """
        opcion_salir = input(texto_salir)
        opcion_salir = int(opcion_salir)
        if opcion_salir == 1:
            with open("base_de_datos.json","w") as archivo_db:
                print("Datos Guardados")
                json.dump(lista_estudiantes, archivo_db)
        return
    funcion_menu()    
funcion_menu()
