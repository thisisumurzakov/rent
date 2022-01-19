FROM python:3.8.5

RUN apt-get update
RUN apt-get install -y gdal-bin python3-gdal libpq-dev

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r  requirements.txt

COPY src /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]