FROM ubuntu:latest

MAINTAINER Hamidreza Hosseinkhani "hosseinkhani@live.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# the ports on which the container will listen for connections (Flask apps listen to port 5000, by default)
# I think we can ommit it!
EXPOSE 5000

COPY ./requirements.txt /inpin/requirements.txt

WORKDIR /inpin

RUN pip3 install -r requirements.txt

COPY . /inpin

RUN python3 create_db.py

ENTRYPOINT ["python3"]
CMD ["main.py"]