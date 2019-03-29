FROM ubuntu:16.04
# Set the file maintainer (your name - the file's author)
MAINTAINER Min Zhang



ENV HOMEDIR=/home
ENV PROJECTDIR=/home/blog
ENV BACKENDDIR=/home/blog/backend
WORKDIR $BACKENDDIR
COPY . .

# Install basic apps
RUN mv sources.list /etc/apt/ && apt-get update && apt-get install -y git emacs curl iputils-ping

# Install python/django dependencies 	        	    
RUN apt-get install -y python3 python3-dev python3-pip build-essential libssl-dev libffi-dev  \
     libxml2-dev libxslt1-dev zlib1g-dev supervisor nginx libpq-dev uwsgi-plugin-python3 libcurl4-openssl-dev supervisor
RUN pip3 install -U pip setuptools
#RUN pip3 install uwsgi

# Copy and Install requirements
# (before copying the rest of the code, so docker would cache them and not reinstall)


#COPY requirements.txt .
RUN pip3 install  -i https://pypi.tuna.tsinghua.edu.cn/simple  -r requirements.txt

# Copy all project files	 


# Serve it with nginx/uwsgi    	 
# https://github.com/dockerfiles/django-uwsgi-nginx
# tutorial: https://uwsgi.readthedocs.org/en/latest/tutorials/Django_and_nginx.html	
RUN echo "daemon off;" >> /etc/nginx/nginx.conf    	 
COPY config/backend_nginx.conf /etc/nginx/sites-available/default
COPY config/supervisor.conf /etc/supervisor/conf.d
COPY config/uwsgi.ini $PROJECTDIR
COPY config/uwsgi_params $PROJECTDIR

# Migrate (not sure if it works)
CMD [ "python3", "./manage.py migrate" ]            
# Start supervisor
CMD ["supervisord", "-n"]
