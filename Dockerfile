FROM ubuntu:16.04

RUN apt update
RUN apt upgrade
RUN apt install -y software-properties-common git curl python-pip python-dev build-essential
#RUN apt install -y snapd
#RUN snap install juju --classic
RUN pip install pyyaml
RUN add-apt-repository -y "deb http://osm-download.etsi.org/repository/osm/debian/ReleaseTHREE stable IM osmclient"
RUN curl "http://osm-download.etsi.org/repository/osm/debian/ReleaseTHREE/OSM%20ETSI%20Release%20Key.gpg" | apt-key add -
RUN apt update
RUN apt install -y python-osm-im
