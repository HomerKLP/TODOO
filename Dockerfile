FROM python:3.9.2-slim

ENV PYTHONUNBUFFERED=1 COLUMNS=200 \
    TZ=Asia/Almaty PIP_CONFIG_FILE=/src/pip.conf

ADD ./src/requirements.txt \
    ./src/dev_requirements.txt /src/

RUN apt update -y

# User local alpine repositories
RUN apt install -y gettext \
    && pip install --upgrade pip wheel setuptools \
    # Add project dependencies
    && pip install \
    --no-cache-dir -Ur /src/requirements.txt \
    --no-cache-dir -Ur /src/dev_requirements.txt \
    # Remove build dependencies
    && apt clean

COPY ./src /src

WORKDIR /src
CMD ["./entrypoint.sh"]
