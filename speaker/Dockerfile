FROM resin/rpi-raspbian:stretch

RUN apt-get update
RUN apt-get install -y python3 python3-pip wget htop vim mc
RUN apt-get install -y swig3.0 python-pyaudio python3-pyaudio sox
RUN pip3 install pyaudio
RUN pip3 install setuptools
RUN pip3 install paho-mqtt 
RUN apt-get install -y libatlas-base-dev
RUN apt-get install -y alsa-utils unzip openssh-server libpython2.7 bzip2
RUN apt-get update
RUN apt-get install -y vorbis-tools 

ENV AUDIODEV=plughw:CARD=CameraB409241,DEV=0
ENV AUDIODRIVER=alsa

ENV MQTT_PORT=1883
ENV MQTT_HOST=10.10.0.137
ENV MQTT_TOPIC=raspi-1/speak
ENV TTS_HOST=10.10.0.137
ENV TTS_PORT=1995
ENV AUDIO_DEVICE=dev:plughw:CARD=sndrpihifiberry,DEV=0

WORKDIR /home

COPY asoundrc /root/.asoundrc
COPY soundclient.py /home/soundclient.py

ENTRYPOINT ["python3", "/home/soundclient.py"]
