per avviare portainer

docker run -d -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:2.11.1

guida elk pazzeska
https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose
