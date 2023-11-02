# Event-Driven-Arc-withRabbitMQ-Python-Docker

 
HOW TO USE RABBITMQ TO PYTHON APP

1.   HOW TO CONNECT DOCKER WITH DJANGO:
after installing django, rest_framework
create your  dockerfile and compose (Backend,db)
first make backend ,  check docker then add db and check again, meanwhile you could have sqlite3 , no problem 
later we will delte it (whateve you do check  from brower )
to test if docker runs or not:
$ docker-compose up , then 
click on brower:http://127.0.0.1:8000/
if server works ,then Bingo !

stop your dockerfile running !!!

2.in your db configure  a  database name here is admin name , etc 
 docker-compose exec backend sh
<bACKEND IS THE NAME OF OUR APP HERE >


setting add:
CORS_ORIGIN_ALLOW_ALL = True
 'corsheaders.middleware.CorsMiddleware',
    'rest_framework',
    'corsheaders',
    'products'


 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'admin',
         'USER': 'root',
         'PASSWORD': '9818',
         'HOST': 'db',
         'PORT': '3306',
     }
 }

  
3.CREATE A NEW APP VIA  DOCKERFILE :

after we hard code our DB in settings and map to our DB , 

we run a docker command inside the container:
$ docker-compose exec backend sh
# python manage.py startapp product


4.
REMOVE sqlite3 from setting

restart dockerfile again 

5.
make things inside your app as following:
in app make model , serializer 
views.py  urls.py 

migration from docker
PS C:\mydrive\DjangoProjects2023\EventDrivenArchWithRabbitMQ> docker-compose exec backend sh
# python manage.py makemigrations
...............migrate

6.serialziers

7.views.py
urls.py

8.check on Postman
GET :http://127.0.0.1:8000/api/products
we will see empty array .Bingo

* in Browser you also can check if it displays
http://127.0.0.1:8000/api/products

then in views.py  create:


check in postman again if it is ok 
http://127.0.0.1:8000/api/products

make  def create......
POST , body, raw, json   ==>send
{
    "title":"title",
    "image":"image"
}



you have to create  account in  CLOUD rabbitMQ to get the URL then go to your page
https://api.cloudamqp.com/console/c7a46-bd99-4396-9c05-4b685887999978787
Copy the URL in there , paste for  your connection in consumer/producer


