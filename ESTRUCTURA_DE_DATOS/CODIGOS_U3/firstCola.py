from queue import Queue

class Servicio:
    def __init__(self):
        self.colas = {}

    def llegada_cliente(self, servicio):
        if servicio not in self.colas:
            self.colas[servicio] = Queue()
        numero_atencion = self.colas[servicio].qsize() + 1
        self.colas[servicio].put(numero_atencion)
        return numero_atencion

    def atender_cliente(self, servicio):
        if servicio in self.colas and not self.colas[servicio].empty():
            numero_atendido = self.colas[servicio].get()
            return numero_atendido
        else:
            return "No hay clientes en espera para el servicio {}".format(servicio)

def main():
    servicio = Servicio()

    while True:
        entrada = input("Ingrese 'C' seguido del número de servicio para llegada de cliente o 'A' seguido del número de servicio para atender cliente: ").split()
        
        if len(entrada) != 2:
            print("Entrada inválida. Por favor, ingrese 'C' seguido del número de servicio o 'A' seguido del número de servicio.")
            continue

        accion, numero_servicio = entrada
        if accion == 'C':
            numero_atencion = servicio.llegada_cliente(numero_servicio)
            print("El cliente ha llegado al servicio {} y su número de atención es: {}".format(numero_servicio, numero_atencion))
        elif accion == 'A':
            numero_atendido = servicio.atender_cliente(numero_servicio)
            print("Se está llamando al cliente {} del servicio {}".format(numero_atendido, numero_servicio))
        else:
            print("Acción no reconocida. Por favor, ingrese 'C' para llegada de cliente o 'A' para atender cliente.")

if __name__ == "__main__":
    main()

