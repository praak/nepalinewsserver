FROM python:3

RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi

COPY ./source /opt/api

RUN pip3 install -r /opt/api/requirements.txt

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

EXPOSE 8000
CMD uwsgi --ini /opt/api/uwsgi.ini
