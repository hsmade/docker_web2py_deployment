FROM debian:jessie
RUN apt-get update && apt-get install -y --no-install-recommends supervisor unzip curl lighttpd python-pip && rm -rf /var/lib/apt/lists/*
WORKDIR /opt/
RUN curl -o /tmp/web2py.zip http://www.web2py.com/examples/static/web2py_src.zip && unzip /tmp/web2py.zip && rm /tmp/web2py.zip && mv web2py/handlers/fcgihandler.py web2py/ && rm -r web2py/applications/welcome web2py/applications/examples && find /var/log -type f -delete
RUN pip install redis
ADD lighttpd-sv.conf fcgihandler.conf /etc/supervisor/conf.d/
ADD lighttpd.conf /etc/lighttpd/lighttpd.conf
ADD route.py /opt/web2py/
ADD start.sh /
EXPOSE 80
VOLUME /opt/web2py/applications/init
CMD ["/start.sh"]
