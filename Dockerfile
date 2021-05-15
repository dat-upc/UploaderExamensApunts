FROM python:3.8-buster

ENV MYSQL_ROOT_PASSWORD password

RUN apt-get update
RUN apt-get install -y python3 python3-venv python3-pip git mariadb-server mariadb-client libz-dev libjpeg-dev libfreetype6-dev python3-dev
RUN pip3 install Django mysqlclient django-simple-captcha

# Create the database.
RUN service mysql start &&\
    mysql -u root -p${MYSQL_ROOT_PASSWORD} -e "CREATE DATABASE dat_uploader;" &&\
    mysql -u root -p${MYSQL_ROOT_PASSWORD} -e "CREATE USER 'dat'@'localhost' IDENTIFIED BY 'password'" &&\
    mysql -u root -p${MYSQL_ROOT_PASSWORD} -e "GRANT ALL PRIVILEGES ON dat_uploader.* TO 'dat'@'localhost'" &&\
    mysql -u root -p${MYSQL_ROOT_PASSWORD} -e "FLUSH PRIVILEGES"

WORKDIR /app
COPY . /app

CMD service mysql start && python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000

EXPOSE 8000
