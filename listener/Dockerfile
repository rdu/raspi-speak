FROM resin/rpi-raspbian:stretch

RUN apt-get update
RUN apt-get install -y python2.7 python-pip wget htop vim mc
RUN apt-get install -y swig3.0 python-pyaudio python2.7-pyaudio sox
RUN apt-get install -y libatlas-base-dev
RUN apt-get install -y alsa-utils unzip openssh-server libpython2.7 bzip2
RUN pip install pyaudio
RUN pip install setuptools
RUN pip install paho-mqtt

ENV AUDIODEV=plughw:CARD=CameraB409241,DEV=0
ENV AUDIODRIVER=alsa

ENV SPEECH_HOST=10.10.0.137
ENV SPEECH_PORT=9000
ENV MQTT_PORT=1883
ENV MQTT_HOST=10.10.0.137
ENV MQTT_TOPIC=raspi-1/hotword

WORKDIR /home

ADD https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/rpi-arm-raspbian-8.0-1.1.1.tar.bz2  /home

RUN tar xfj /home/rpi*.bz2 -C /home --strip-components=1

COPY asoundrc /root/.asoundrc
COPY snowboydecoder.py /home
COPY models /home/models
COPY train.sh /home
COPY server.py /home

ENTRYPOINT ['bin/bash']
