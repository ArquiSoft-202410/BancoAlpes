import pika
import json

rabbit_host = '10.128.0.57'
rabbit_user = 'banco_alpes'
rabbit_password = 'banco_alpes_password'
exchange = 'ASR2_Availability'
topic = 'load_balancer'

def sendRequest(formData):
    payload = json.dumps(formData)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='topic')
    channel.basic_publish(exchange=exchange, routing_key=topic, body=payload)
    print(formData)
    connection.close()