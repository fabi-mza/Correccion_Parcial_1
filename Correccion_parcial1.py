# Correccion parcial 1

# Sistema de Control de Inventario
herramientas = []
existencias = []

while True:
    print('''
          1. Carga Inicial de Herramientas:
          2. Carga de Existencias:
          3. Visualización de Inventario
          4. Consulta de Stock:
          5. Reporte de Agotados:
          6. Alta de Nuevo Producto:
          7. Actualización de Stock (Venta/Ingreso):
          8. Salir:
          ''')
    
    opcion = input("Elija una opción del menú que desee ingresar: ").strip()
    
    match opcion:
        case "1":
            # Registrar los nombres de las herramientas que se pondrán a la venta
            # Se debe preguntar al usuario la cantidad de herramientas a cargar y
            # se debe usar una estructura pertinente. En caso de nombre vacío o duplicado
            # se debe seguir pidiendo hasta que sea correcto respetando la cantidad de herramientas
            # que el usuario indicó antes de la carga.
            cant_str = input("Ingrese la cantidad de herramientas a cargar: ")
            while not cant_str.isdigit():
                cant_str = input("Error: Ingrese la cantidad de herramientas a cargar: ")
            cant = int(cant_str)

            for i in range(cant):
                while True:
                    nom = input(f"Ingrese el nombre de {i+1} herramienta: ").strip().capitalize()
                    if nom == "":
                        print("Error: el nombre no puede estra vacío.")
                        continue

                    existe = False
                    for h in herramientas:
                        if h == nom:
                            existe = True
                    if existe:
                        print("Error: Ya existe.")
                    else:
                        herramientas.append(nom)
                        existencias.append(0)
                        break
                    
            
        case "2":
            # Ingresar la cantidad de unidades para cada herramienta registrada previamente,
            # respetando el orden de ingreso. Cuando el usuario ingresa existencias,
            # el sistema debe mostrar por pantalla el nombre de la herramienta.
            if len(herramientas) == 0:
                print("Error: No hay herramientas cargadas. Seleccione opción 1.")
            
            else:
                for i in range(len(herramientas)):
                    while True:
                        print(f"Ingrese la cantidad de stock de herramientas para {herramientas[i]}: ")
                        stock_str = input("Cantidad: ")

                        if stock_str.isdigit():
                            stock = int(stock_str)
                            existencias[i] = stock
                            print("La carga de stock se realizó correctamente.")
                            break
                        else:
                            print("Error: Ingrese un número positivo.")
            

        case "3":
            # Mostrar el listado completo de herramientas junto a su stock actual.
            if len(herramientas) == 0:
                print("Error: No hay herramientas cargadas. Seleccione opción 1.")
            
            else:
                for i in range(len(herramientas)):
                    print(f"\nHerramienta {herramientas[i]} - Stock: {existencias[i]}")

            
        case "4":
            # Buscar una herramienta por su nombre y mostrar cuántas unidades hay disponibles.
            busqueda = input("Ingrese el nombre de la herramienta a buscar: ").strip().capitalize()
            
            if busqueda in herramientas:
                indice = herramientas.index(busqueda)
                print(f"Herramienta: {herramientas[indice]} - Stock: {existencias[indice]}")

            else:
                print("Error: No hay herramienta cargada con ese nombre. Seleccione opción 1.")

            
        case "5":
            # Listar únicamente aquellos productos cuyo stock sea igual a cero.
            print("\n---PRODUCTOS CON 0 STOCK---")
            encontrado = False

            for i in range(len(existencias)):
                if existencias[i] == 0:
                    print(f"Herramienta: {herramientas[i]} (Sin stock).")
                    encontrado = True
            if not encontrado:
                print("Error: No hay Herramientas con 0 stock.")


        case "6":
            # Permitir agregar solo una nueva herramienta al final de las listas con su stock inicial.
            # En caso de nombre vacío, nombre duplicado o valor de existencia negativo
            # se debe volver al menú principal mostrando por pantalla el motivo
            nueva_herr = input("Ingrese la nueva herramienta: ").strip().capitalize()
            if nueva_herr == "":
                print("Error: No puede estar vacío")
            elif nueva_herr in herramientas:
                print("La Herramienta ingresada ya existe.")
            else:
                nuevo_stock = input("Ingrese cantidad de herramienta: ").strip() # es string
                if nuevo_stock.isdigit():
                    herramientas.append(nueva_herr)
                    existencias.append(int(nuevo_stock)) # lo convertimos en entero
                    print("Herramienta agregada correctamente.")
                else:
                    print("Error: El valor a ingresar debe ser un número positivo.")


            
        case "7":
            # Venta: Disminuir el stock tras validar que hay unidades suficientes.
            # Ingreso: Aumentar el stock por reposición de mercadería.
        
            # 1. Elegir el tipo de operación
            actualizar = input("Ingrese la opción que desea realizar, Venta (V) o Ingreso (I): ").strip().upper()
            
            while actualizar != "V" and actualizar != "I":
                actualizar = input("Error: Debe ingresar V o I: ").strip().upper()

            # 2. Identificar la herramienta
            busqueda = input("Ingrese el nombre de la herramienta a modificar: ").strip().capitalize()
            
            if busqueda in herramientas:
                # Si la herramienta existe, obtenemos su posición (índice)
                indice = herramientas.index(busqueda)
                stock_actual = existencias[indice]
                
                # 3. Pedir la cantidad y validar que sea un número
                cant_input = input(f"Ingrese la cantidad de unidades para la operación: ")
                
                if cant_input.isdigit():
                    cantidad = int(cant_input)
                    
                    # --- LÓGICA DE VENTA ---
                    if actualizar == "V":
                        if stock_actual >= cantidad:
                            existencias[indice] = stock_actual - cantidad
                            print(f"Venta exitosa. Stock actualizado de {busqueda}: {existencias[indice]}")
                        else:
                            print(f"Error: Stock insuficiente. Solo hay {stock_actual} unidades disponibles.")
                    
                    # --- LÓGICA DE INGRESO ---
                    elif actualizar == "I":
                        existencias[indice] = stock_actual + cantidad
                        print(f"Ingreso exitoso. Stock actualizado de {busqueda}: {existencias[indice]}")
                
                else:
                    print("Error: La cantidad debe ser un número entero positivo.")
            
            else:
                print(f"Error: La herramienta '{busqueda}' no se encuentra en el inventario.")

            

            
        case "8":
            print("Saliendo del sistema, gracias por usar nuestros servicios.")
            break
        case _:
            print("Error: Debe ingresar un número del 1 al 8.")