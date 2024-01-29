FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /morni

RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    postgis

COPY . /morni
RUN pip3 install -r requirements.txt
