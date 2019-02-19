FROM alpine:latest

RUN apk add python3

RUN mkdir /app
COPY . /app