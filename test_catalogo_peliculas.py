from dominio.Pelicula import Pelicula
from servicio.catalogo_pelicula import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Peliculas')
        print('2. Listar Peliculas')
        print('3. Eliminar Peliculas')
        print('4. Salir')
        opcion = int(input('Escribe una opcion (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('Ingrese el nombre del pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_pelicula()

    except Exception as e:
        print(e)
        opcion = None
else:
    print('Salimos del programa...')