# UploaderExamensApunts
Webapp to upload exams, notes, etc. to the website.

## Installation ##
### Development ###
This installation notes are for a development environment. For a production environment please see the *nginx* section below.

1. Install required software:
```
sudo apt install python3 python3-venv python3-pip git mysql-server mysql-client python3-mysqldb
```

2. Create a virtual environment:
```
python3 -m venv UploaderExamensApunts
cd UploaderExamensApunts
source bin/activate
```

3. Install Django:
```
pip3 install Django
```

4. Configure the database:
```
sudo mysql
mysql> CREATE DATABASE dat_uploader;
mysql> CREATE USER 'dat'@'localhost' IDENTIFIED BY 'password';
mysql> GRANT ALL PRIVILEGES ON dat_uploader.* TO 'dat'@'localhost';
```
During this step you should follow the instructions in `UploaderExamensApunts/settings_secret.readme`.

5. Configure the app:
```
git clone https://github.com/dat-upc/UploaderExamensApunts.git
cd UploaderExamensApunts
python3 manage.py makemigrations
python3 manage.py migrate
```

6. Run the app:
```
python3 manage.py runserver <IP>:<PORT>
```

### nginx ###
1. Follow steps 1-4 from the previous section.
2. 