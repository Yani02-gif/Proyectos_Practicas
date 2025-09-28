import random
import string
import time 
def generar_contraseña(longitud=8):
    caracteres= string.ascii_letters + string.digits + "!@#$%&*()-_*=<>?¿"
    return"".join(random.choice(caracteres) for i in range(longitud))

def login(): 
    contraseña_sistema= generar_contraseña()
    print("Bienvenido al sistema de gestion de ElectroSmart")
    print("Su contraseña temporal es:",contraseña_sistema)
    print("Ingrese la contraseña para continuar (maximo 5 intentos)")
    intentos = 0
    max_intentos= 5
    while intentos < max_intentos:
        ingreso= input("Ingrese la contraseña: ")
        if ingreso == contraseña_sistema:
            print("Contraseña correcta, Bienvenido Usuario!")
            print("-"*50)
            return True
        else:
            intentos += 1
            print(f"Contraseña incorrecta. Intento {intentos} de 5")
    print("Se han superado los intentos permitidos. Usuario bloqueado por 60 segundos.")
    time.sleep(60)
    print("Intente iniciar sesion nuevamente.")
    return login()

catalogo= {
    "televisores": [
     {"nombre":"Smart TV Samsung 50 4k", 
      "precio":650,
      "stock":4,
      "descripcion":"Resolucion 4K con control por voz."},
     {"nombre":"Philips 43",
      "precio":370,
      "stock":6,
      "descripcion":"Televisor LED Full HD con buena calidad de imagen y eficiencia energética."},
      {"nombre":"LG OLED 55",
       "precio":1200,
       "stock":3,
       "descripcion":"Pantalla OLED con negros puros y colores vibrantes, ideal para cine o gaming."}, 
      {"nombre":"Samsung Neo QLED 8K 65",
       "precio":3500,
       "stock":2,
       "descripcion":"Resolución altísima y tecnología de escalado de imagen."},
      {"nombre":"Sony Bravia 50",
       "precio":730,
       "stock":3,
       "descripcion":"Diseño plano, resolución 4K y Android TV integrado."},
      {"nombre":"Samsung 55 Curvo",
       "precio":880,
       "stock":2,
       "descripcion":"Pantalla curva para una mejor experiencia!"}
    ],
    "celulares": [
        {"nombre":"Samsung Galaxy A15",
        "precio":280,
        "stock":7,
        "descripcion":"Un smartphone moderno con pantalla AMOLED, Android 14 y buenas cámaras para su rango de precio."},
        {"nombre":"Moto E13",
        "precio":120,
        "stock":8,
        "descripcion":"Teléfono accesible, ideal para funciones básicas, con Android Go y batería duradera."},
        {"nombre":"Xiaomi Redmi Note 13",
        "precio":260,
        "stock":6,
        "descripcion":"Excelente relación calidad/precio, con pantalla AMOLED, buen rendimiento y cámara de 108 MP."},
        {"nombre":"Iphone 15 Pro",
        "precio":1600,
        "stock":3,
        "descripcion":"Procesador A17 Pro, diseño en titanio, cámara avanzada y ecosistema iOS."},
        {"nombre":"Alcatel 2053D",
        "precio":50,
        "stock":9,
        "descripcion":"Celular con tapa, botones grandes, pantalla clara y funciones básicas como linterna y radio FM."}
    ],
    "computadoras":[
        {"nombre":"HP Pavilion 15",
         "precio":750,
         "stock":4,
         "descripcion":"Notebook con procesador Intel Core i5, 8 GB de RAM y SSD de 512 GB. Ideal para uso diario y trabajo."},
        {"nombre":"AMD Ryzen 5",
         "precio":400,
         "stock":1,
         "descripcion":"Torre con Ryzen 5 5500G, 16 GB RAM, SSD de 480 GB, y grafica integrada buena opción para oficina o gaming."},
        {"nombre":"Lenovo",
         "precio":670,
         "stock":3,
         "descripcion":"Todo en uno con pantalla de 23.8”, procesador AMD Ryzen 3 o 5, diseño compacto y elegante."},
         {"nombre":"Samsung Galaxy Tab A9",
         "precio":300,
         "stock":8,
         "descripcion":"Tablet con pantalla de 11, Android, ideal para entretenimiento y educación."},
         {"nombre":"Exo Cloud E15",
         "precio":180,
         "stock":7,
         "descripcion":"Netbook liviana y económica con windows 10."}
    ],
    "Accesorios de informatica":[
        {"nombre":"Teclado Logitech K380",
         "precio":35,
         "stock":6,
         "descripcion":"Teclado inalámbrico compacto, compatible con Windows, macOS, Android y más."},
        {"nombre":"Mouse 1850",
         "precio":18,
         "stock":6,
         "descripcion":"Mouse inalámbrico simple, ergonómico y económico."},
        {"nombre":"Parlante Genius SP ",
         "precio":45,
         "stock":8,
         "descripcion":"Parlantes de escritorio con sonido estéreo potente y diseño elegante de madera."},
         {"nombre":"Webcam Logitech C920",
         "precio":90,
         "stock":5,
         "descripcion":"Webcam Full HD 1080p con excelente calidad de imagen y micrófono estéreo integrado."},
         {"nombre":"Router TP Link",
         "precio":40,
         "stock":5,
         "descripcion": "Router Wi-Fi de doble banda con buena cobertura y velocidad, ideal para hogares conectados."},
         {"nombre":"Kingston 64 GB",
         "precio":7,
         "stock":15,
         "descripcion":"Pendrive USB 3.2 rápido y confiable, con tapa protectora y diseño práctico."},
         {"nombre":"WD Elements 1TB",
         "precio":70,
         "stock":6,
         "descripcion":"Disco duro externo portátil, con conexión USB 3.0, ideal para respaldos o almacenamiento adicional."}
    ],
    "Electrodomesticos pequeños":[
         {"nombre":"Microondas BGH",
         "precio":110,
         "stock":5,
         "descripcion":"Microondas digital de 20 litros con grill, múltiples niveles de potencia y funciones automáticas."},
        {"nombre":"Licuadora philips",
         "precio":45,
         "stock":10,
         "descripcion":"Licuadora con jarra de plástico de 1.5L, cuchillas resistentes y motor de 400W."},
        {"nombre":"Tostadora atma",
         "precio":25,
         "stock":15,
         "descripcion":"Tostadora eléctrica para dos rebanadas, con control de temperatura y expulsión automática."},
         {"nombre":"Liliana AP950",
         "precio":28,
         "stock":12,
         "descripcion":"Pava eléctrica de acero inoxidable, con corte automático, base giratoria 360° y visor de nivel de agua."},
         {"nombre":"Nescafe Dolce",
         "precio":90,
         "stock":4,
         "descripcion":"Cafetera automática para cápsulas, diseño compacto y múltiples niveles de intensidad."},
    ],
    "Electrodomesticos grandes":[
         {"nombre":"Heladera Samsung",
         "precio":950,
         "stock":3,
         "descripcion":"Heladera con freezer superior, tecnología No Frost, eficiencia energética A+ y capacidad de 300L."},
        {"nombre":"Lavarropa Drean",
         "precio":420,
         "stock":5,
         "descripcion":"Lavarropas automático de carga frontal, 6 kg de capacidad, múltiples programas y bajo consumo."},
        {"nombre":"Cocina Longvie",
         "precio":470,
         "stock":5,
         "descripcion":"Cocina a gas con horno autolimpiante, encendido eléctrico y 4 hornallas."},
         {"nombre":"Horno Electrico",
         "precio":80,
         "stock":8,
         "descripcion":"Horno eléctrico de 38 litros con convección, grill y múltiples niveles de temperatura."},
         {"nombre":"Lavavajillas",
         "precio":790,
         "stock":3,
         "descripcion":"Lavavajillas de 14 cubiertos, eficiencia energética A++, varios programas y función media carga."},
    ],
    "Audio y Sonido":[
         {"nombre":"Sony WH520",
         "precio":75,
         "stock":12,
         "descripcion":"Auriculares inalámbricos Bluetooth, con buena autonomía (hasta 50 h) y sonido balanceado."},
        {"nombre":"Parlantes Bluetooth",
         "precio":120,
         "stock":8,
         "descripcion":"Parlante Bluetooth portátil, resistente al agua, con gran potencia y graves profundos."},
        {"nombre":"LG XBOOM",
         "precio":450,
         "stock":4,
         "descripcion":"Equipo de sonido potente con iluminación LED, efectos DJ y conectividad Bluetooth."},
         {"nombre":"Samsung HW-B550",
         "precio":200,
         "stock":5,
         "descripcion":"Barra de sonido con subwoofer inalámbrico, Dolby Audio y conectividad HDMI/Optical."},
         {"nombre":"Philips FX10",
         "precio":240,
         "stock":5,
         "descripcion":"Minicomponente compacto con 300W, CD, Bluetooth, USB y entrada auxiliar."},
    ],
    "Gaming":[
        {"nombre":"PlayStation 5",
         "precio":1500,
         "stock":2,
         "descripcion":"Consola de última generación con SSD ultrarrápido, gráficos 4K y control DualSense."},
        {"nombre":"Xbox Series S",
         "precio":750,
         "stock":2,
         "descripcion":"Consola digital compacta, con excelente rendimiento en juegos next-gen a 1440p."},
        {"nombre":"Nintendo Switch",
         "precio":900,
         "stock":3,
         "descripcion":"Consola híbrida con pantalla OLED de 7, ideal para jugar en casa o portátil."},
         {"nombre":"Xbox Wireless Controller",
         "precio":80,
         "stock":10,
         "descripcion":"Mando compatible con Xbox y PC, con conexión Bluetooth, diseño ergonómico y gran respuesta."},
         {"nombre":"HyperX Cloud",
         "precio":65,
         "stock":8,
         "descripcion":"Auriculares con micrófono, sonido envolvente y gran comodidad para largas sesiones de juego."},
         {"nombre":"Samsung Odyssey G5 27",
         "precio":450,
         "stock":3,
         "descripcion":"Monitor curvo QHD, 144Hz, 1ms de respuesta, ideal para gaming competitivo."}
    ],
    "Camaras y fotografia":[
         {"nombre":"Canon Powershot",
         "precio":350,
         "stock":6,
         "descripcion":"Cámara compacta con zoom óptico 40x, estabilizador de imagen y grabación 4K."},
        {"nombre":"Canon EOS",
         "precio":2100,
         "stock":2,
         "descripcion":"Cámara mirrorless APS-C con sensor de 32.5 MP, ráfaga de 30 fps y video 4K 60p. Ideal para fotografía avanzada."},
        {"nombre":"DJI mini 4 pro",
         "precio":1600,
         "stock":4,
         "descripcion":"Drone liviano con cámara 4K, sensores de obstáculos y hasta 34 minutos de vuelo. Apto para hobby y trabajo profesional."},
         {"nombre":"Manfrotto Compact Action",
         "precio":60,
         "stock":14,
         "descripcion":"Trípode liviano con rótula ergonómica, ideal para cámaras compactas y DSLR pequeñas."},
         {"nombre":"Canon EF",
         "precio":130,
         "stock":5,
         "descripcion":"Lente fijo luminoso, excelente para retratos, con gran calidad de imagen y enfoque silencioso."},
    ]}

def mostrar_catalogo():
    print("Catalogo de productos:")
    for categoria, productos in catalogo.items(): 
        print(f"Categoria:{categoria.capitalize()}")
        for producto in productos:
            print(f"Producto:{producto['nombre']}")
            print(f"Precio:${producto['precio']}")
            print(f"Stock:{producto['stock']}")
            print(f"Descripcion:{producto['descripcion']}")
            print("-" *50) #usamos esto para generar una linea entre cada elemento y que se lea mejor

carrito= []

def buscar_producto(nombre ): #si el producto encontrado es igual al producto escrito por el usuario, devuelve el producto, si no, devuelve vacio
    for productos in catalogo.values():
        for producto in productos:
            if producto["nombre"].lower() == nombre.lower():
                return producto
    return None 

def agregar():
    nombre= input("Ingrese el nombre del producto que desea: ").lower() #agrega los productos al carrito
    producto=buscar_producto(nombre)
    if not producto: 
        print("Este producto no esta en el catalogo.")
        return
    
    cantidad= input("Ingrese la cantidad deseada: ")
    if not cantidad.isdigit() or int(cantidad) <= 0:
        print("Ingrese una cantidad valida(numero entero).")
        return
    
    cantidad = int(cantidad)
    if cantidad > producto["stock"]:
        print(f"No hay suficiente stock. El stock disponible es de {producto['stock']}")
        return
    
    producto["stock"] -= cantidad #resta lo que el usuario tomo al stock que ya hay y agrega el producto al carrito
    carrito.append({
        "nombre": producto["nombre"],
        "precio": producto["precio"],
        "cantidad": cantidad
    })
    print(f"{producto['nombre']} x {cantidad} fue agregado al carrito")
    
def mostrar_carrito(): #muestra el carrito junto al precio base
    if not carrito:
        print("El carrito esta vacio.")
        return
    
    print("Carrito:")
    total= 0
    for item in carrito:
        subtotal= item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{item['nombre']} - ${item['precio']} x {item['cantidad']}= ${subtotal}")
    print(f"total a pagar: ${total}")
def eliminar_del_carrito(): #elimina articulos del carrito y en el proceso confirma si el usuario esta seguro o no
    if not carrito:
        print("El carrito esta vacio.")
        return
    
    nombre=input("Ingrese el nombre del producto a eliminar: ").lower()
    for item in carrito:
        if item['nombre'].lower() == nombre.lower():
            confirmacion= input(f"Estas seguro que desea eliminar '{nombre}' del carrito? (si/no): ").lower()
            if confirmacion == "si":
                carrito.remove(item)
                producto = buscar_producto(nombre)
                if producto:
                    producto["stock"] += item ["cantidad"] #al eliminar el elemento del carrito, le volvemos a sumar la cantidad que el usuario tomo al stock
                print(f"{nombre} fue eliminado del carrito.")
            else:
                print("Eliminacion Cancelada.")
            return
    print("el producto no esta en el carrito")
    
def finalizar_compra(): #al momento de finaliazar la compra, le muestra los metodos de pago disponibles
    if not carrito:
        print("El carrito esta vacio.")
        return
    total= sum(item["precio"] * item["cantidad"] for item in carrito)
    print("METODOS DE PAGO:")
    print("Efectivo(1)")
    print("Tarjeta de credito(2)")
    print("Bitcoin(3)")
    pago=input("Que metodo de pago desea?: ")
    if pago == "1" or pago == "3":
        print(f"Total a pagar: ${total:.2f}")
    elif pago == "2":
        print("PLANES DE CUOTAS")
        print("3 cuotas tiene un interes del 12%")
        print("6 cuotas tiene un interes del 18%")
        print("12 cuotas tiene un interes del 36%")
        plan= input("Seleccione el plan deseado(3,6 o 12): ")
        if plan == "3":
            subtotal1= (total * 0.12) + total
            cuota= subtotal1 / 3
        elif plan == "6":
            subtotal1= (total * 0.18) + total
            cuota= subtotal1 / 6
        elif plan == "12":
            subtotal1= (total * 0.36) + total
            cuota= subtotal1 / 12
        else:
            print("Ingrese un plan de cuotas valido.")
            return
        print(f"Total a pagar con interes: {subtotal1:.2f}")
        print(f"En {plan} comodas cuotas de {cuota:.2f} al mes")
    else:
        print("Ingrese un metodo de pago valido.")
        return
    print(f"Gracias por tu compra!")
    carrito.clear()
    
def menu():
    while True:
        print("Menu de compras:")
        print("1.Agregar producto al carrito")
        print("2.Ver carrito")
        print("3.Eliminar producto del carrito")
        print("4.Finalizar compra")
        print("5. Salir")
        opcion= input("Seleccione una opcion: ")
        
        if opcion == "1":
            agregar()
        elif opcion == "2":
            mostrar_carrito()
        elif opcion == "3":
            eliminar_del_carrito()
        elif opcion == "4":
            finalizar_compra()
        elif opcion == "5":
            print("Saliendo del menu de compras. Muchas gracias!")
            break
        else:
            print("Ingrese una opcion valida.")

def main():
    login()
    mostrar_catalogo()
    menu()
    
main()