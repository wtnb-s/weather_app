FROM php:7.0-apache
RUN apt update && apt install -y --no-install-recommends nano libicu-dev \
    && rm -rf /var/lib/apt/lists/*
RUN apt upgrade -y
RUN apt dist-upgrade -y
RUN apt autoremove -y
RUN apt autoclean -y
RUN apt install wget
RUN apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libbz2-dev cmake liblzma-dev
RUN cd /usr/local/src/
RUN wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
RUN tar xvfzp Python-3.8.0.tgz
RUN cd Python-3.8.0
RUN ./configure 
RUN make
RUN make altinstall
RUN pip3.8 install --upgrade pip
RUN pip3.8 install matplotlib
RUN pip3.8 install numpy
RUN pip3.8 install pandas
RUN pip3.8 install geopandas
RUN pip3.8 install descartes

WORKDIR /root
RUN docker-php-ext-install intl pdo pdo_mysql
CMD $PRJ/bin/cake server  -H 0.0.0.0 -p 80
EXPOSE 80
