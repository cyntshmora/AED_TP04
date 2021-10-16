import files_manager
import books_manager


def main():
    list_books = []
    matrix_books = None
    file_name = "populares.dat"
    # variables para la interfaz de usuario
    decoration_points = '*' * 40
    decoration_lines = "-" * 80
    list_not_founded_message = "No hemos podido encontrar un listado de datos, por favor verifique para que podamos procesar su pedido"
    user_menu = '''\nMENU DE OPCIONES
        1. Opcion 1
        2. Opcion 2
        3. Opcion 3
        4. Opcion 4
        5. Opcion 5
        6. Opcion 6
        7. Opcion 7
        0. Salir del programa
    '''
    selection = 1

    # menu de opciones
    while selection != "0":
        print(user_menu)
        selection = input("> Ingrese la opción elegida: ")

        if selection == "1":
            print("\n--- OPCION 1 ---")
            print("Cargando listado...")
            list_books = files_manager.get_list_from_file()
            print("Carga completada.")

        #La opcion dos no hace esto en la consigna, acá lo hice solo para testear cosas
        elif selection == "2":
            print("\n--- OPCION 2 ---")
            if len(list_books) > 0:
                print(decoration_points + " LIBROS REGISTRADOS " + decoration_points)
                books_manager.show_books_list(list_books)
                print("LIBROS MOSTRADOS: " + str(len(list_books)))
            else:
                print(list_not_founded_message)

        elif selection == "4":
            print("\n--- OPCION 2 ---")
            if len(list_books) > 0:
                print("Generando matriz de rating")
                matrix_books = books_manager.generate_mat(27, 21)
                books_manager.fill_ratings_matrix(list_books, matrix_books)
                print("Matriz generada")
            else:
                print(list_not_founded_message)

        elif selection == "6":
            print("\n--- OPCION 6 ---")
            if len(list_books) > 0:
                if matrix_books is not None:
                    result = files_manager.generate_books_file(matrix_books, file_name)
                    print("Archivo generado, registros guardados: ", result)
                else:
                    print("La matriz de libros aún no ha sido generada")
            else:
                print(list_not_founded_message)

        elif selection == "7":
            print("\n--- OPCION / ---")
            if matrix_books is not None:
                files_manager.show_file(file_name)
            else:
                print(list_not_founded_message)

        elif selection != "0":
            print("\nIngrese una opcion válida")

    print("\n\n", decoration_lines, "\nGracias por usar este programa\n\t\tCynthia Mora")


if __name__ == '__main__':
    main()
