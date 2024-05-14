import time
from connect import create_client # Importar función de conexión


def subscribe_topic(client, topico): # Función para subscribir a topico elegido
    client.subscribe(topico)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Interrupción del teclado detectada, desconectando...")
    finally:
        client.unsubscribe(topico) # Desubscribirse al tópico


def subTopic():
    client = create_client()  # Variable para que carguen los mensajes
    time.sleep(1)  # 1s de delay para que carguen bien los demas prints.

    while True:
        print("=============================")
        print("Elija una opción")
        print("=============================")
        print("1. Animales/gatos")
        print("2. Animales/perros")
        print("3. Todos los tópicos")
        print("4. Salir")

        eleccion = input()

        if eleccion == "1":
            print("Elegido tópico gatos")
            subscribe_topic(client, "animales/gatos")

        elif eleccion == "2":
            print("Elegido tópico perros")
            subscribe_topic(client, "animales/perros")

        elif eleccion == "3":
            print("Elegido tópico animales")
            subscribe_topic(client, "animales/#")

        elif eleccion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__": # Acá agrego esto para que no se llame la función al ejecutar main.py
    subTopic()
