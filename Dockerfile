FROM python:3.12

COPY . /morni
WORKDIR /morni

RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    postgis

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
