from pub import pubTopic
from sub import subTopic

def main():
    while True:
        print("=============================")
        print("Elija una opción")
        print("=============================")
        print("1. Subscribirse a un Topico")
        print("2. Publicar en un Topico")
        print("3. Salir")

        eleccion = input()

        if eleccion == "1":
            subTopic()

        elif eleccion == "2":
            pubTopic()

        elif eleccion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
