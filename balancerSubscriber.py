import subprocess
from sys import path
from os import environ
import django
import pika
import json

path.append('BancoAlpes/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'BancoAlpes.settings')
django.setup()

rabbit_host = '10.128.0.57'
rabbit_user = 'banco_alpes'
rabbit_password = 'banco_alpes_password'
exchange = 'ASR2_Availability'
topic = 'load_balancer'

### Funciones de Respuesta ###
def callback(ch, method, properties, body):
    value = json.loads(body)
    print(value)
    try:
        subprocess.run(['sudo', 'docker', 'restart', 'kong'], check=True)
        print("Kong has been restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to restart Kong: {e}")

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
