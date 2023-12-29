FROM python:3.9.9

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt

COPY ./test_sf .
ADD ./start.sh /
COPY ./.env .
RUN chmod +x /start.sh

EXPOSE 8000
