FROM nginx:1.19.2

RUN rm /etc/nginx/conf.d/*
ADD reverse-proxy.conf /etc/nginx/conf.d/reverse-proxy.conf 
ADD nginx.conf /etc/nginx/nginx.conf
