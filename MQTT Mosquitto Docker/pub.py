import time
from connect import create_client


def publish_topic(client, topico, mensaje):
    client.publish(topico, mensaje)


def pubTopic():
    client = create_client()  # Variable para que carguen los mensajes
    time.sleep(1)  # 1s de delay para que carguen bien los demas prints.

    while True:
        print("=============================")
        print("Elija una opción")
        print("=============================")
        print("1. Animales/gatos")
        print("2. Animales/perros")
        print("3. Salir")

        eleccion = input()

        if eleccion == "1":
            while True:
                try:
                    mensaje = input("Ingrese un mensaje: ")
                    publish_topic(client, "animales/gatos", mensaje)
                    print(
                        f'Usted ha enviado "{mensaje}" con exito al tópico animales/gatos'
                    )
                except KeyboardInterrupt:
                    print(
                        "Interrupción del teclado detectada, volviendo al menú principal..."
                    )
                    break

        elif eleccion == "2":
            while True:
                try:
                    mensaje = input("Ingrese un mensaje: ")
                    publish_topic(client, "animales/perros", mensaje)
                    print(
                        f'Usted ha enviado "{mensaje}" con exito al tópico animales/perros'
                    )
                except KeyboardInterrupt:
                    print(
                        "Interrupción del teclado detectada, volviendo al menú principal..."
                    )
                    break

        elif eleccion == "3":
            print("Saliendo del programa...")
            client.disconnect()
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__": # Acá agrego esto para que no se llame la función al ejecutar main.py
    pubTopic()
