# syntax=docker/dockerfile:1
FROM ubuntu
COPY linkfinder.py /opt
COPY flag.txt /flag.txt

RUN apt update -y && apt upgrade -y
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

RUN apt install -y apache2
RUN apt install -y php
RUN apt install -y python3
RUN apt install wget -y

RUN apt install gnupg2 -y
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable 
RUN apt install pip -y
RUN python3 -m pip install pyppeteer



RUN mkdir /var/www/html/links
RUN rm /var/www/html/index.html

COPY index.php /var/www/html/

RUN mkdir /var/www/.local

RUN chown www-data -R /var/www/html/*
RUN chown www-data -R /var/www/.local
RUN chown www-data -R /opt
RUN chmod 777 /var/www/*
RUN mv /flag.txt /flag$(echo -n $(cat /flag.txt) | md5sum | cut -d " " -f 1).txt
RUN chown www-data:www-data /flag*
RUN service apache2 restart

