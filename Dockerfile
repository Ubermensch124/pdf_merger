FROM python:3.11.2-slim-buster

WORKDIR /app

COPY main.py /app/
COPY requirements.txt /app/

RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]