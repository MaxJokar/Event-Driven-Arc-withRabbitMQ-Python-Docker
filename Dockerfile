FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
# we are copying inside the docker container
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
#  current files are connected to the docker
COPY . /app  

# inside the docker container => add in docker-compose(for RabbitMQ)
# CMD python manage.py runserver 0.0.0.0:8000