"""
whenever we send from POSTMAn /api/products we get consumer
in Terminal first 
in second Terminal where we used Docker shell 
we type:
$ docker-compose exec backend sh 
# python consumer.py 

"""
import pika, json, os, django
from products.models import Product

# params = pika.URLParameters('your_rabbitmq_url')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://qqclhqyu:3DJRZ5L0NQLNY3d-8gwkD5NhvJ1IJZck@cow.rmq2.cloudamqp.com/qqclhqyu')
# connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    # print(body)
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id = id)
    product.likes = product.likes + 1
    product.save()
    print("Products likes increased ")
    


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

# Terminal:
# eventdrivenarchwithrabbitmq-queue-1    | Started Consuming
# eventdrivenarchwithrabbitmq-queue-1    | Received in admin
# eventdrivenarchwithrabbitmq-queue-1    | b'hello'
# eventdrivenarchwithrabbitmq-queue-1    | Received in admin
# eventdrivenarchwithrabbitmq-queue-1    | b'hello'