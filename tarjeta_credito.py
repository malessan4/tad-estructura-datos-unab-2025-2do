# TAD de una tarjeta de credito

class TajetaCredito(object):
    nro_id = None
    nombre_cliente = None
    codigo_seguridad = None
    fecha_vencimiento = None
    limite_credito = None
    saldo_actual = None

    def __init__(self, nro_id, nombre_cliente, codigo_seguridad, fecha_vencimiento, limite_credito):
        self.nro_id = str(nro_id)
        self.nombre_cliente = nombre_cliente
        self.codigo_seguridad = str(codigo_seguridad)
        self.fecha_vencimiento = fecha_vencimiento
        self.limite_credito = float(limite_credito)
        self.saldo_actual = 0.00


    def __str__(self):
        nro_protegido = '**** **** **' + self.nro_id[-4:]
        return (f"--- Tarjeta de Crédito ---\n"
                f"Titular: {self.nombre_cliente}\n"
                f"Número: {nro_protegido}\n"
                f"Vencimiento: {self.fecha_vencimiento}\n"
                f"Límite: ${self.limite_credito:,.2f}\n"
                f"Saldo Deuda: ${self.saldo_actual:,.2f}")
    


    def comprar(self, precio):
        credito_disponible = self.limite_credito - self.saldo_actual
        if precio < credito_disponible:
            self.saldo_actual += precio
            self.limite_credito -= precio
            print(f"Compra exitosa por el monto de: ${precio}")
            return
        else:
            print(f"No tiene limite suficientes para la compra de: ${precio} ")
            return
        

mi_tarjeta = TajetaCredito(123476546789, "Matias Daniel Alessandrello", 123, "01-27", 1000000)
print(mi_tarjeta)
print()
mi_tarjeta.comprar(2000000)
print()
mi_tarjeta.comprar(200000)
print()
print(mi_tarjeta)
