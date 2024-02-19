from circular_list import CircularList

carousel = CircularList()

while True:
    print("Menu Carrusel\n")
    print("1. Girar el carrusel")
    print("2. Parar el carrusel")
    print("3. Agregar persona al carrusel")
    print("4. Siguiente asiento")
    print("5. Desocupar a una persona del carrusel")
    print("6. Mostrar asiento")
    print("7. Desocupar todos los asientos")
    print("8. Salir")

    carousel_options = input("Ingrese una opcion (1-8): ")

    if carousel_options == "1":
        carousel.rotate()

    elif carousel_options == "2":
        carousel.stop()

    elif carousel_options == "3":
        person = input('Ingrese el nombre de la persona que ingresara al carrusel: ')
        carousel.add_element(person)
        print(f"{person} se subio al carrrusel")

    elif carousel_options == "4":
        carousel.next_seat()

    elif carousel_options == "5":
        clear_out = input("Ingrese el nombre de la persona que desea bajar del carrusel: ")
        get_on = input("Ingrese el nombre de la persona que se subira al carrusel: ")
        carousel.edit_element(clear_out, get_on)

    elif carousel_options == "6":
        carousel.show_seat()

    elif carousel_options == "7":
        carousel.clear_circular_list()
        
    elif carousel_options == "8":
        print("Saliendo del programa...")
        break
    else:
        print("Ingrese una opcion valida")