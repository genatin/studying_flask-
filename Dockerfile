FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

RUN apk add --update py-pip bash nano
RUN pip install --upgrade pip

COPY . /web
WORKDIR /web
RUN pip install --no-cache-dir -r requirements.txt
