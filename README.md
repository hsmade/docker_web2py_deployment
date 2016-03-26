# docker_web2py_deployment
A project to demonstrate how to run multiple scalable web2py pods behind an nginx proxy with automated "Let's encrypt" certificates

This project uses multiple different projects glued together:

- https://github.com/docker/dockercloud-haproxy
- https://github.com/rckrdstrgrd/nginx-proxy
- https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion
- http://web2py.com
- https://hub.docker.com/_/postgres/

You can specify what web2py app directory to mount in web2py/docker-compose.yml
