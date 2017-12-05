FROM resin/rpi-raspbian:stretch

RUN apt-get update
RUN apt-get install -y python3 python3-pip wget htop vim mc
RUN apt-get install -y swig3.0 python-pyaudio python3-pyaudio sox
RUN pip3 install pyaudio
RUN apt-get install -y libatlas-base-dev
RUN apt-get install -y alsa-utils unzip openssh-server libpython2.7 bzip2

ENV AUDIODEV=plughw:CARD=CameraB409241,DEV=0
ENV AUDIODRIVER=alsa

WORKDIR /home

ADD https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/rpi-arm-raspbian-8.0-1.1.1.tar.bz2  /home

RUN tar xfj rpi*.bz2

COPY asoundrc /root/.asoundrc
COPY idle.sh /home/idle.sh

ENTRYPOINT /home/idle.sh
