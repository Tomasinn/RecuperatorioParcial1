productos = ["Sonrisas 45g", "Pepitos 50g", "Oreos 50g", "Zucaritas 100g"] #Lista de los productos en string
print(productos)
stock = ["3", "5", "3", "3"] #Lista de stock en string tambien
sin_stock = 0
fin_ciclo = 0
contador_productos = 4

while fin_ciclo == 0: #Ciclo para repetir el menu hasta que se active el numero 5
    print("Menu de opciones")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")

    opcion_menu = int(input("Ingrese la opcion: ")) #Menu en numeros enteros
    if opcion_menu == 1:
        contador_productos = contador_productos + 1
        nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
        productos.append(nuevo_producto)
        stock.append("0")
        print("Producto agregado")
    elif opcion_menu == 2:
        for i in range(contador_productos):
             if stock[i] == "0":
                print(f"El producto {productos[i]} no tiene stock")
                sin_stock += 1    
        if sin_stock == 0:
            print("Todos los productos cuentan con stock")
    elif opcion_menu == 3:
        for i in range(contador_productos):
            print(f"{i+1}.{productos[i]}") #Mini menu para ver los productos 
        opcion_menu_3 = int(input("Ingrese a que producto cambiarle el stock: "))
        opcion_menu_3 = opcion_menu_3 - 1
        nuevo_stock = input("Ingrese de cuanto quiere que sea el stock: ")
        stock[opcion_menu_3] = nuevo_stock
        print("Stock actualizado")
    elif opcion_menu == 4:
        for i in range(contador_productos):
            print(f"{i+1}.{productos[i]}")
    elif opcion_menu == 5:
        print("Saliendo del programa")
        fin_ciclo = 1 #Aqui termina el While
    else:
        opcion_menu = input("Opcion no existente, ingrese otro valor: ") #Si se ingresa un valor que no esta indicado en las opciones se pedira otro numero
    
    
    
    
            
    