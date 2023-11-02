"""
HOW TO USE RABBITMQ TO PYTHON APP
we are connecting RabbitMQ to Python , here is the following
"""
import pika, json

params = pika.URLParameters('amqps://qqclhqyu:3DJRZ5L0NQLNY3d-8gwkD5NhvJ1IJZck@cow.rmq2.cloudamqp.com/qqclhqyu')
# params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(params)
channel = connection.channel()



# Test : to send event for updating,deleting or creating product 
# def publish():
    
#     channel.basic_publish(exchange='', routing_key='admin', body='hello')



#  we want to see every time the product deleted, updated or  created 
def publish(method, body ):    
    properties = pika.BasicProperties(method)
    #  we have to convert to json before we send  as following:
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
    
#  POSTMAN GET   :http://127.0.0.1:8000/api/products
#  we send some data from POSTMAN to test POST :body, raw jason

# {
#     "title":"title",
#     "image":"image"
# }

    
    

 