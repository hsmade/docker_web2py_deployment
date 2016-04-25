# docker_web2py_deployment
A project to demonstrate how to run multiple scalable web2py pods behind an nginx proxy with automated "Let's encrypt" certificates

This project uses multiple different projects glued together:

- https://github.com/docker/dockercloud-haproxy
- https://github.com/rckrdstrgrd/nginx-proxy
- https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion
- http://web2py.com
- https://hub.docker.com/_/postgres/

You can specify what web2py app directory to mount in web2py/docker-compose.yml

# Layout
This project sets up one web2py pod (from web2py/) that consists of:
- A postgres database
- A web2py container which you can scale (by starting multiple)
- A web2py scheduler container which you can scale (by overriding the command)
- A haproxy that points to the web2py containers and automatically updates on scale changes
On this pod (in the docker-compose.yml file), you specify the public hostname to use, so the final front end can create virtual hosts and certificates.
You can get to the stats of the haproxy by connecting to the specified port (12346 in this case)

It also sets up a pod with an nginx proxy and letsencrypt container that automatically update when new web2py pods are created. The proxy points to the haproxy and th letsencrypt container will create certificates for all hostnames automatically.
