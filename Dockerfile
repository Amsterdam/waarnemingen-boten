FROM amsterdam/python
MAINTAINER datapunt@amsterdam.nl

ENV PYTHONUNBUFFERED 1
ENV CONSUL_HOST=${CONSUL_HOST:-notset}
ENV CONSUL_PORT=${CONSUL_PORT:-8500}

RUN apt update && apt upgrade -y && apt autoremove -y

RUN apt install -y \
        wget \
        vim \
        postgresql \
        postgresql-contrib \
        gdal-bin \
    && pip install --upgrade pip 

RUN mkdir -p /app /static /deploy 

COPY src/requirements.txt /app/
RUN pip install -r requirements.txt

COPY src /app
COPY deploy /deploy/
WORKDIR /app

CMD ["/deploy/docker-run.sh"]
