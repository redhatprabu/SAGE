FROM centos

MAINTAINER redhatprabu@gmail.com

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
      && yum update -y \
      && yum install -y python-pip \
      && pip install flask

COPY . /src

EXPOSE 5000

CMD cd /src && python home.py
