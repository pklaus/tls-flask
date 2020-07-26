# tls-flask

This image runs a minimal Flask app on port 443 generating a
self-signed certificate when starting up (due to `--cert=adhoc`).

This is useful if you quickly need an SSL/TLS server up and running
in Docker or Kubernetes to test a load balancer etc.

Run the image with port 443 of your host forwarded to the container:

    docker run --rm -it -p 443:443 pklaus/tls-flask

Now when you go to <https://localhost:443>, you'll be served with an HTML
page showing a lot of the properties of the flask.Request object, such as headers
your browser sent or the remote IP that made the connection (`REMOTE_ADDR`).

Alternative, if you want to use your own certs:

```sh
docker run \
  --rm -it \
  -p 443:443 \
  -v /your-cert.pem:cert.pem:ro \
  -v /your-key.pem:key.pem:ro \
  pklaus/tls-flask \
  flask run --host 0.0.0.0 --cert=cert.pem --key=key.pem
```
