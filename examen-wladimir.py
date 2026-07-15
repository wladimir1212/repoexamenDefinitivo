peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except:
            print("Debe seleccionar una opción válida")

def cupos_por_genero(genero):
    total = 0
    for codigo in peliculas:
        if peliculas[codigo][1].lower() == genero.lower():
            total += cartelera[codigo][1]
    print("El total de cupos disponibles es:", total)
def busqueda_por_rango_de_precio(precio_min, precio_max):
    lista = []
    for codigo  in cartelera:
        precio = cartelera[codigo][0]
        cupos = cartelera[codigo][1]
        if precio_min <= precio <= precio_max and cupos != 0:
            lista.append(peliculas[codigo][0] + "--" + codigo)
    lista.sort()
    if len(lista) == 0:
        print("No hay películas en ese rango de precios.")
    else:
        print("Las películas encontradas son:", lista)

def buscar_codigo(codigo):
    codigo = codigo.upper()
    for cod in peliculas:
        if cod.upper() == codigo:
            return True
    return False
def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo):
        codigo = codigo.upper()
        cartelera[codigo][0] = nuevo_precio
        return True
    return False
def validar_codigo(codigo):
    if codigo.strip() == "":
        return False
    if buscar_codigo(codigo):
        return False
    return True
def validar_texto(texto):
    if texto.strip() == "":
        return False
    return True
def validar_duracion(duracion):
    return duracion > 0
def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ["A", "B", "C"]
def validar_3d(valor):
    return valor.lower() in ["s", "n"]
def validar_precio(precio):
    return precio > 0
def validar_cupos(cupos):
    return cupos >= 0

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion,idioma, es3d, precio, cupos):

    if buscar_codigo(codigo):
        return False
    peliculas[codigo] = [
        titulo,
        genero,
        duracion,
        clasificacion.upper(),
        idioma,
        es3d
    ]
    cartelera[codigo] = [precio, cupos]
    return True

def eliminar_pelicula(codigo):

    if buscar_codigo(codigo):
        codigo = codigo.upper()
        del peliculas[codigo]
        del cartelera[codigo]
        return True
    return False
def menu():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")

        opcion = leer_opcion()

        if opcion == 1:
            genero = input("Ingrese género a consultar: ")
            cupos_por_genero(genero)
        elif opcion == 2:
            while True:
                try:
                    precio_min = int(input("Ingrese precio mínimo: "))
                    precio_max = int(input("Ingrese precio máximo: "))
                    if precio_min >= 0 and precio_max >= 0 and precio_min <= precio_max:
                        break
                    else:
                        print("Debe ingresar valores válidos.")
                except:
                    print("Debe ingresar valores enteros")
            busqueda_por_rango_de_precio(precio_min, precio_max)
        elif opcion == 3:
            while True:
                codigo = input("Ingrese código de película: ").upper()
                while True:
                    try:
                        nuevo_precio = int(input("Ingrese nuevo precio: "))
                        if nuevo_precio > 0:
                            break
                        else:
                            print("El precio debe ser mayor que cero.")
                    except:
                        print("Debe ingresar un número entero.")
                if actualizar_precio(codigo, nuevo_precio):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                seguir = input("¿Desea actualizar otro precio (s/n)? ").lower()
                if seguir == "n":
                    break
        elif opcion == 4:
            codigo = input("Ingrese código de película: ").upper()
            titulo = input("Ingrese título: ")
            genero = input("Ingrese género: ")
            try:
                duracion = int(input("Ingrese duración (minutos): "))
            except:
                duracion = -1

            clasificacion = input("Ingrese clasificación: ").upper()
            idioma = input("Ingrese idioma: ")
            es3d = input("¿Es 3D? (s/n): ").lower()
            try:
                precio = int(input("Ingrese precio: "))
            except:
                precio = -1
            try:
                cupos = int(input("Ingrese cupos: "))
            except:
                cupos = -1
            if not validar_codigo(codigo):
                print("Código inválido")
            elif not validar_texto(titulo):
                print("Título inválido")
            elif not validar_texto(genero):
                print("Género inválido")
            elif not validar_duracion(duracion):
                print("Duración inválida")
            elif not validar_clasificacion(clasificacion):
                print("Clasificación inválida")
            elif not validar_texto(idioma):
                print("Idioma inválido")
            elif not validar_3d(es3d):
                print("Valor de 3D inválido")
            elif not validar_precio(precio):
                print("Precio inválido")
            elif not validar_cupos(cupos):
                print("Cupos inválidos")
            else:
                if es3d == "s":
                    es3d = True
                else:
                    es3d = False
                if agregar_pelicula(codigo, titulo, genero, duracion,clasificacion, idioma, es3d,precio, cupos):
                    print("Película agregada")
                else:
                    print("El código ya existe")
        elif opcion == 5:
            codigo = input("Ingrese código de película: ").upper()
            if eliminar_pelicula(codigo):
                print("Película eliminada")
            else:
                print("El código no existe")
        elif opcion == 6:
            print("Programa finalizado.")
            break
if __name__ == "__main__":
    menu()