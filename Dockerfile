FROM python:3-alpine
RUN apk add build-base
ADD requirements.txt /requirements.txt
RUN python3 -m pip install -r /requirements.txt
ADD . /app
WORKDIR /app
CMD python3 .
