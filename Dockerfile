FROM debian:10-slim

RUN apt-get update
RUN apt-get install \
    --no-install-recommends --no-install-suggests \
    python3 \
    python3-pip \
    python3-pkg-resources \
    #python3-flask \
    #python3-openssl \
    #python3-pygments \
    -yq

RUN pip3 install flask pyopenssl pygments

COPY *.py /
COPY templates /templates

ENV FLASK_APP=/server.py FLASK_ENV=production
CMD flask run --host 0.0.0.0 --port 443 --cert=adhoc
# Alternative, if you want to use your own certs:
#CMD flask run --host 0.0.0.0 --cert=cert.pem --key=key.pem
