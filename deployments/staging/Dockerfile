FROM python:3.8.5

RUN apt-get update
RUN apt-get install -y gdal-bin python3-gdal libpq-dev

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements requirements/
RUN pip install --upgrade pip && pip install -r  requirements/staging.txt

COPY src /app

RUN echo yes | python manage.py collectstatic --noinput

EXPOSE 8000


CMD ["gunicorn", "--bind", ":8000", "config.wsgi:application"]