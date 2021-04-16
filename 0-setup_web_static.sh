#!/usr/bin/env bash
# Installs nginx and sets up web servers for web_static deployment
apt-get -y update
apt-get -y upgrade
apt-get -y install nginx
sed -i "/listen \[::\]:80 default_server/ a\\\trewrite ^/redirect_me https://github.com/andylopezr permanent;" /etc/nginx/sites-available/default
sed -i "/listen \[::\]:80 default_server/ a\\\tadd_header X-Served-By \"\$HOSTNAME\";" /etc/nginx/sites-available/default
sed -i "/redirect_me/ a\\\terror_page 404 /404.html;" /etc/nginx/sites-available/default
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
service nginx restart