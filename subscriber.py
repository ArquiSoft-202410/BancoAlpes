from BancoAlpes import settings
from sys import path
from os import environ
from random import randint
import django
import pika
import vonage
import json

path.append('BancoAlpes/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'BancoAlpes.settings')
django.setup()

rabbit_host = '10.128.0.57'
rabbit_user = 'banco_alpes'
rabbit_password = 'banco_alpes_password'
exchange = 'ASR1_OTPs'
topic = 'OTPs'

### Funciones de Respuesta ###
def callback(ch, method, properties, body):
    value = json.loads(body)
    value['codigo'] = randint(10000, 99999)
    print("Received %r" % value)
    send_sms(value)

def send_sms(value):
    client = vonage.Client(key=settings.VONAGE_API_KEY, secret=settings.VONAGE_API_SECRET)
    sms = vonage.Sms(client)
    message = f"OTP: Hola, {value['nombres']}, para validar tu informacion ingresa el siguiente codigo: {value['codigo']}\n\n"
    recipient_number = f'57{value['numero']}'
    response_data = sms.send_message({
        "from": "Vonage APIs",
        "to": recipient_number,
        "text": message,
    })
    if response_data["messages"][0]["status"] == "0":
        print("Mensaje enviado exitosamente.")
    else:
        print(f"Error al enviar mensaje: {response_data['messages'][0]['error-text']}")

### Conexión a RabbitMQ ###
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=rabbit_host,
        credentials=pika.PlainCredentials(rabbit_user, rabbit_password)
    )
)
channel = connection.channel()
channel.exchange_declare(exchange=exchange, exchange_type='topic')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=topic)
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

### Inicio de consumo ###
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
