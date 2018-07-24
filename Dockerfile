FROM 	tiangolo/uwsgi-nginx:python2.7
MAINTAINER Michel Belleau <michel.belleau@malaiwah.com>

RUN	apt-get update && apt-get install -y mtr-tiny iputils-ping iperf3 nmap unbound-host supervisor
RUN	mkdir -p /var/log/supervisor

COPY	requirements.txt glass.py /srv/lg/
COPY	extra /srv/lg/extra/
COPY	static /srv/lg/static/
COPY	templates /srv/lg/templates/
RUN 	pip install -r /srv/lg/requirements.txt

RUN	/srv/lg/extra/adduser.sh

COPY	supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD	["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
EXPOSE	8080
EXPOSE	5201
