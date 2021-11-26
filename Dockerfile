FROM python:3.8-slim-buster

RUN mkdir /code
WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 80

ENTRYPOINT uvicorn main:app --port 80 --host 0.0.0.0