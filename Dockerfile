FROM pyro225/freecad-docker:latest

MAINTAINER jdlubrano <jdlubrano@gmail.com>

USER root

RUN apt-get update && \
  apt-get install -y python-setuptools freecad-dev && \
  apt-get clean

RUN easy_install pip

RUN mkdir /app
WORKDIR /app

ARG PORT=5000
ENV PORT $PORT
EXPOSE $PORT

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "main.py"]
