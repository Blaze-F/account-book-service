FROM python:3.10.8

MAINTAINER jh Hwang <daeda766@gmail.com>

# RUN mkdir /server/docker
ADD . /server/docker
WORKDIR /server/docker 
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


EXPOSE 8000
