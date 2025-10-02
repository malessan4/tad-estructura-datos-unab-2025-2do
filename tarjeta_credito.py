# TAD de una tarjeta de credito

class TajetaCredito(object):
    nro_id = None
    nombre_cliente = None
    codigo_seguridad = None
    fecha_vencimiento = None
    limite_credito = None
    saldo_actual = None
    tipo_tarjeta = None
    estado_tarjeta = None
    movimientos = None

    def __init__(self, nro_id, nombre_cliente, codigo_seguridad, fecha_vencimiento, limite_credito, tipo_tarjeta, estado_tarjeta):
        self.nro_id = str(nro_id)
        self.nombre_cliente = nombre_cliente
        self.codigo_seguridad = str(codigo_seguridad)
        self.fecha_vencimiento = fecha_vencimiento
        self.limite_credito = float(limite_credito)
        self.saldo_actual = 0.00
        self.tipo_tarjeta = tipo_tarjeta
        self.estado_tarjeta = estado_tarjeta
        self.movimientos = []


    def __str__(self):
        nro_protegido = '**** **** **' + self.nro_id[-4:]
        return (f"--- Tarjeta de Crédito ---\n"
                f"Titular: {self.nombre_cliente}\n"
                f"Número: {nro_protegido}\n"
                f"Vencimiento: {self.fecha_vencimiento}\n"
                f"Límite: ${self.limite_credito:,.2f}\n"
                f"Saldo Deuda: ${self.saldo_actual:,.2f}\n"
                f"Tipo Tarjeta: {self.tipo_tarjeta}\n"
                f"Estado: {self.estado_tarjeta}")

    


    def comprar(self, precio):
        credito_disponible = self.limite_credito - self.saldo_actual
        if self.estado_tarjeta != "Activa":
            print(f"Compra rechazada por su tarjeta esta {self.estado_tarjeta}")
            return 
        elif precio <= credito_disponible:
            self.saldo_actual += precio
            self.limite_credito -= precio
            movimiento = {
                "tipo": "Compra",
                "monto": precio,
            }
            self.movimientos.append(movimiento)
            print(f"Compra exitosa por el monto de: ${precio:,.2f}")
            return
        else:
            print("No tiene limite disponible para la compra")
            return

        
    def bloquear(self, estado_tarjeta):
        self.estado_tarjeta = estado_tarjeta
        print(f"Su tarjeta ha sido {self.estado_tarjeta}")
        return
        
    def mostrar_movimientos(self):
        print("***** MOVIMIENTOS DE COMPRAS *****")
        if not self.movimientos:
            print("No hay movimientos en esta cuenta")
        for mov in self.movimientos:
            print(f"{mov['tipo']} {mov['monto']:,.2f}")


# Programa Principal

mi_tarjeta = TajetaCredito(123476546789, "Matias Daniel Alessandrello", 123, "01-27", 1000000, "VISA", "Activa")
print(mi_tarjeta)
print()
mi_tarjeta.comprar(2000000)
print()
mi_tarjeta.comprar(200000)
print()
print(mi_tarjeta)
print()
mi_tarjeta.bloquear("Bloqueada")
print()
mi_tarjeta.comprar(50000)
print()
print(mi_tarjeta)
print()
mi_tarjeta.bloquear("Activa")
print()
mi_tarjeta.comprar(50000)
print()
print(mi_tarjeta)
print()
mi_tarjeta.mostrar_movimientos()