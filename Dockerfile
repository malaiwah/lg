FROM 	tiangolo/uwsgi-nginx:python2.7

RUN	apt-get update
RUN	apt-get install -y mtr-tiny iputils-ping

COPY	requirements.txt glass.py /srv/lg/
COPY	extra /srv/lg/extra/
COPY	static /srv/lg/static/
COPY	templates /srv/lg/templates/
RUN 	pip install -r /srv/lg/requirements.txt

RUN	/srv/lg/extra/adduser.sh

WORKDIR	/srv/lg
CMD	uwsgi -p 16 --http-socket 0.0.0.0:8080 --uid lg -w glass:app
EXPOSE	5000
