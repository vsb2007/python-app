FROM ubuntu

USER root
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
RUN apt-get -y install tzdata python3-dev python3 python3-pip


WORKDIR /app

RUN pip3 install flask flask_sockets

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]