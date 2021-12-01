# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app

COPY fizz_buzz.py .

CMD [ "python3" , "fizz_buzz.py"]
