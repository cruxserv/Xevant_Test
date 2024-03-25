FROM python:3.9-slim-buster

WORKDIR /

RUN apt-get update
RUN apt-get -y install gcc build-essential unixodbc-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

VOLUME /files_outbound

CMD ["python", "file_parser.py"]

