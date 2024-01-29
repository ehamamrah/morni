FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin

RUN mkdir /morni
WORKDIR /morni
COPY . /morni
RUN pip3 install -r requirements.txt
