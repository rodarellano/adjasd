cantidadparacetamol=0
cantidadtapsin=0
cantidadvitaminac=0
cantidadnastizol=0
cantidadibuprofeno=0
paracetamol=2490
tapsin=4990
vitaminaC=990
nastizol=6690
ibuprofeno=2500


while True:
    print("""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        BIENVENIDO A NUESTRA FARMACIA!!
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n
        1.- Paracetamol $2490
        2.- Tapsin $4990
        3.- Vitamina C $990
        4.- Nastizol $6690
        5.- Ibuprofeno $2500
        6.- Salir
        """)
    try:
        opciones = int(input("¿Que medicamento necesita?: "))
        if opciones >= 1 and opciones <=6:
            if opciones == 1:   #ESCOGE EL PARACETAMOL
                cantidadparacetamol+=1
                print("Has agregado 1 Paracetamol")
            elif opciones == 2:   #ESCOGE EL TAPSIN
                cantidadtapsin+=1
                print("Has agregado 1 Tapsin")
            elif opciones == 3:  #ESCOGE LA VITAMINA C
                cantidadvitaminac+=1
                print("Has agregado 1 Vitamina C")
            elif opciones == 4:   #ESCOGE EL NASTIZOL
                cantidadnastizol+=1
                print("Has agregado 1 Nastizol")
            elif opciones == 5:
                cantidadibuprofeno+=1
            elif opciones == 6:   #PROCEDE A SALIR DEL MENÚ PARA MOSTRAR LA CANTIDAD DE CADA MEDICAMENTO, EL TOTAL DE LA COMPRA Y EL IVA
                subtotal = (paracetamol*cantidadparacetamol)+(tapsin*cantidadtapsin)+(vitaminaC*cantidadvitaminac)+(nastizol*cantidadnastizol)
                iva=0.19*subtotal
                print(f"""
                **********************
                |Paracetamol: {cantidadparacetamol}      |
                |Tapsin: {cantidadtapsin}           |
                |Vitamina C: {cantidadvitaminac}       |
                |Nastizol: {cantidadnastizol}         |
                ********************** \n
                ********************            
               * tu compra: {subtotal}       *
               * iva acumulado: {iva} *
               * total: {subtotal+iva}         *
                ********************""")
                if subtotal >=500000:
                    print("EXCELENTE, SE CUMPLIO LA META!!!")
                else:
                    print(f" la meta: 500000 \n ganancias: {subtotal} \n DEBEMOS REALIZAR MAS OFERTAS PARA ALCANZAR LA META!!!")
                break
    except ValueError:
        print("INGRESE UNA OPCION VALIDA!!")