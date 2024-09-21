FROM nvidia/cuda:12.6.1-runtime-ubuntu20.04

RUN apt-get update &&\
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata

RUN apt update && apt install -y \
    wget \
    libgl1-mesa-glx \
    libglib2.0-0 \
    python3.9 \
    python3.9-dev \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./app ./app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--worker-class", "eventlet", "app.main:app"]
