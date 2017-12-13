FROM ubuntu:16.04

MAINTAINER Atul Abhishek <atul.abhishek@openebs.io>

RUN rm -rf /var/lib/apt/*

RUN apt-get clean

RUN apt-get -y update

RUN apt-get -y upgrade

RUN apt-get -y install git

RUN apt-get install -y software-properties-common && apt-get install -y python-pip

RUN pip install GitPython && pip install pyyaml

ADD launch.sh /

COPY testgit.py /demo/

RUN chmod +x /launch.sh

CMD /launch.sh
