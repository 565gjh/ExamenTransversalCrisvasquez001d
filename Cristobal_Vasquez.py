productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
            }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
        }

print("""
     *** MENU PRINCIPAL ***
        1. Stock marca.
        2. Búsqueda por precio.
        3. Actualizar precio.
        4. Salir.
      """)
while True:
    def stock_marca():
        print ("Productos en stock:") 
        for marca in stock:
            print (marca)
           

    def busqueda_precio(precio):
        for marca in stock:
            if stock[marca][0] >= precio:
                print ("El precio mínimo para la marca " + marca + " es de " + str(stock[marca][0]) + " pesos.")
        
            else:
                print ("No hay productos con precio inferior a " + str(precio) + " pesos.")

    def actualizar_precio(marca, precio):
        stock[marca][0] = precio
        print ("El precio de la marca " + marca + " ha sido actualizado a " + str(precio) + " pesos.")

    opc = int(input ("Ingrese opción: "))
    if opc == 1:
        stock_marca()
    elif opc == 2:
            print ("Ingrese precio mínimo:")
            precio = int(input (""))
            print ("Ingrese precio máximo:")
            precio_max = int(input (""))
            for marca in stock:
                if stock[marca][0] >= precio and stock[marca][0] <= precio_max:
                    print (f"Los notebooks entre los precios consultas son: {marca}")
                    

    elif opc == 3:
        print ("Ingrese modelo a actualizar:")
        marca = input ("")
        print ("Ingrese precio nuevo:")
        precio = int(input (""))
        actualizar_precio(marca, precio)
        print ("Precio actualizado!!")

        print ("Desea actualizar otro precio (si/no)?:")
        opc = input ("")
        if opc == "si":
            opc = 2
        elif opc == "no":
            opc = 1

    elif opc == 4:
        print ("Programa finalizado.") 
        break 