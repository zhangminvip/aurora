FROM ubuntu:16.04

# Set the file maintainer (your name - the file's author)
MAINTAINER Min Zhang



ENV HOMEDIR=/home
ENV PROJECTDIR=/home/blog
ENV FRONTENDDIR=/home/blog/frontend
WORKDIR $FRONTENDDIR
COPY . .

# Install Nginx.	
RUN mv sources.list /etc/apt/ && apt-get update && apt-get install -y nginx

# Turn off daemon mode
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

# Copy frontend files



# Copy nginx config
RUN rm /etc/nginx/sites-enabled/default
COPY frontend_nginx.conf /etc/nginx/sites-enabled


# Define default command.
CMD ["nginx"]

# Expose ports.
EXPOSE 8080
       
