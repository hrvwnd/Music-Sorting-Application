FROM python:3.6
WORKDIR /app
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python", "app.py"]
COPY . .
