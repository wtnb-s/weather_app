FROM php:7.2-apache
RUN apt-get update && apt-get install -y --no-install-recommends \
        nano \
        libicu-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root
RUN docker-php-ext-install intl pdo pdo_mysql
RUN mkdir /root/weather_app
COPY weather_app /root/weather_app
CMD $PRJ/bin/cake server  -H 0.0.0.0 -p 80
EXPOSE 80
