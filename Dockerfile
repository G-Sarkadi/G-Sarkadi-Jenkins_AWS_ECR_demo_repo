FROM python:3.10-alpine

EXPOSE 5000

# docker-compose uses SIGTERM and SIGKILL to stop an app, Flask needs SIGINT
STOPSIGNAL SIGINT

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
