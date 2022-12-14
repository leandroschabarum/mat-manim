# https://docs.manim.community/en/stable/installation/linux.html
FROM python:3.9-slim
LABEL stage=manim_build
USER root

# Install Manim required dependencies
RUN apt update 2>&1 > /dev/null
RUN apt install -y libcairo2-dev libpango1.0-dev ffmpeg pkg-config python3-dev gcc
# Install Manim optional dependencies
RUN apt install -y texlive-full

# Install Manim together with the project requirements
COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR /opt/src
VOLUME [ "/opt/src" ]
CMD [ "/bin/bash" ]
