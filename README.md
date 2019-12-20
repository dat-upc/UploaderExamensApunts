# Description
This repository contains a webapp used to upload exams, notes and other materials to the DAT (Delegació d'Alumnes de Telecomunicacions) website. It is developed using Python3 and the Django framework.

# Source code
All the files in this repository are licensed under the **GNU Affero General Public License 3**, or any later version.

# Installation #
## Development ##
This installation notes are for a development environment. For a production environment please see the **Production** section below.

1. Create the file `UploaderExamensApunts/settings_secret.py`:
```python
# Create a settings_secret.py for DB credentials following this format:
SECRET_KEY_SAVED='SECRET_KEY'
DATABASE_MYSQL="DBName"
USER_NAME="user"
PASSWORD="password"
HOST='127.0.0.1'
TOKEN="TOKEN_TO_UPDATE_SUBJECTS"
```

2. Create migrations directories:
```bash
mkdir uploader/migrations
touch uploader/migrations/__init__.py
mkdir directorySeeker/migrations
touch directorySeeker/migrations/__init__.py
```

3. Install required software:
```
sudo apt install docker.io
```

4. Build the Docker image:
```
docker build --tag=dat-uploader .
```

5. Create the container:

```
docker run -it -p 8000:8000 -v $(pwd):/app dat-uploader
```

To stop and start the container:
```
docker stop <container_id>
docker start -a <container_id>
```

## Production ##
### nginx ###

1. Install required software:
```
sudo apt install python3 python3-venv python3-pip git mysql-server mysql-client python3-mysqldb python3-dev
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
mkdir uploader/migrations
mkdir directorySeeker/migrations
touch uploader/migrations/__init__.py
touch directorySeeker/migrations/__init__.py
python3 manage.py makemigrations
python3 manage.py migrate
```

6. TODO
