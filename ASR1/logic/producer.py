import pika
import json

rabbit_host = '10.128.0.2'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'ASR1_OTPs'
topic = 'OTPs'

def sendRequest(formData):
    payload = json.dumps(formData)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='topic')
    channel.basic_publish(exchange=exchange, routing_key=topic, body=payload)
    print(formData)
    connection.close()