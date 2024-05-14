import paho.mqtt.client as mqtt

# Función para conectar
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Conectado!\nCódigo: {reason_code}")

# Función para manejar los mensajes recibidos
def on_message(client, userdata, message):
    print(f"Mensaje recibido: '{message.payload.decode()}' en el tópico '{message.topic}'")

def create_client():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect("localhost", 1883, 60)
    client.loop_start()
    return client