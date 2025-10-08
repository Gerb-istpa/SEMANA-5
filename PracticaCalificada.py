#1. CATALOGO DE PROPDUCTOS
def crear_catalogo():
    """
    Crea y retorna el catálogo de productos de la tienda.
    
    Returns:
        list: Lista de diccionarios con productos y precios
    """ 
    catalogo=[
        {"nombre": "Laptop", "precio": 1500.20},
        {"nombre": "Smartphone", "precio": 800.00},    
        {"nombre": "Tablet", "precio": 400.00},
        {"nombre": "Monitor", "precio": 300.00},   
        {"nombre": "Teclado", "precio": 100.00}   
    ]
    return catalogo
# ============================================
# 2. FUNCIÓN: CALCULAR DESCUENTO
# ============================================
def calcular_descuento(monto_total):#parametro
    """
    Calcula el descuento aplicable según el monto total de compra.
    
    Args:
        monto_total (float): Monto total de la compra en soles
    
    Returns:
        float: Monto del descuento calculado
    """
    if monto_total < 500:
        descuento = 0
    elif monto_total < 1000:
        descuento = monto_total * 0.05
    elif monto_total < 2500:
        descuento = monto_total * 0.10
    else:
        descuento = monto_total * 0.15
    
    return descuento
# ============================================
# 3. FUNCIÓN: MOSTRAR FACTURA
# ============================================
def mostrar_factura(productos_comprados, subtotal, descuento, total_final):#parametros
    """
    Muestra la factura de compra con formato profesional.
    
    Args:
        productos_comprados (list): Lista de productos comprados
        subtotal (float): Subtotal antes del descuento
        descuento (float): Monto del descuento aplicado
        total_final (float): Total final a pagar
    """
    print("\n" + "=" * 40)
    print("         FACTURA - TECHSTORE PERÚ")
    print("=" * 40)
    print(f"{'Producto':<20} {'Precio':>15}")
    print("-" * 40)

   # Mostrar cada producto comprado
    for producto in productos_comprados:
        print(f"{producto['nombre']:<20} S/ {producto['precio']:>10.2f}")
    
    print("-" * 40)
    print(f"{'Subtotal:':<20} S/ {subtotal:>10.2f}")
    
    # Calcular porcentaje de descuento para mostrarlo
    if subtotal > 0:
        porcentaje = (descuento / subtotal) * 100
    else:
        porcentaje = 0
    
    print(f"Descuento ({porcentaje:.0f}%):     S/ {descuento:>10.2f}")
    print("-" * 40)
    print(f"{'TOTAL A PAGAR:':<20} S/ {total_final:>10.2f}")
    print("=" * 40)

# ============================================
# 4. FUNCIÓN: MOSTRAR CATÁLOGO
# ============================================
def mostrar_catalogo(catalogo):
    """
        Muestra el catálogo de productos disponibles.
    Args:
        catalogo (list): Lista de productos disponibles
     """
    print("\n" + "=" * 40)
    print("      CATÁLOGO DE PRODUCTOS")
    print("=" * 40)
    for i, producto in enumerate(catalogo, 1):
      print(f"{i}. {producto['nombre']} - S/ {producto['precio']:.2f}")   
      print("=" * 40 + "\n")
# ============================================
# 5. PROGRAMA PRINCIPAL
# ============================================

def main(): 
    """
    Función principal que ejecuta el sistema de ventas.
    """
    
    print("=" * 40)
    print("   BIENVENIDO A TECHSTORE PERÚ")
    print("=" * 40)
    # Crear catálogo de productos
    catalogo = crear_catalogo()
    # Mostrar catálogo al cliente
    mostrar_catalogo(catalogo)
    # Lista para almacenar productos comprados
    productos_comprados = []
    subtotal = 0
    
    # Solicitar cantidad de productos a comprar
    
    try:
        cantidad = int(input("\n¿Cuántos productos desea comprar? "))
        if cantidad <= 0:
            print("Debe comprar al menos 1 producto.")
            return
          # Bucle para seleccionar productos
            for i in range(cantidad):
                print(f"\n--- Producto {i + 1} de {cantidad} ---")
                opcion = int(input("Ingrese el número del producto: "))
          # Validar opción  
                if 1 <= opcion <= len(catalogo):#longitud del catalogo
                    producto_seleccionado = catalogo[opcion - 1] #restar 1 para obtener el índice correcto
                    productos_comprados.append(producto_seleccionado) #agregar a la lista
                    subtotal += producto_seleccionado["precio"]#sumar al subtotal o acumulador
                    print(f"✓ {producto_seleccionado['nombre']} agregado (S/ {producto_seleccionado['precio']:.2f})")
                else:
                    print("⚠ Opción inválida. Producto no agregado.")
             # Calcular descuento y total final
                    
            descuento = calcular_descuento(subtotal)#argumento
            total_final = subtotal - descuento
            
            # Mostrar factura
            mostrar_factura(productos_comprados, subtotal, descuento, total_final)#argumentos
        
            print("\n¡Gracias por su compra!")
                  
    except ValueError:
        print("⚠ Error: Debe ingresar un número válido.")        
    except Exception as e:
        print(f"⚠ Error inesperado: {e}")
    
    

# ============================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================

if __name__ == "__main__":
    main()