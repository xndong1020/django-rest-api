### Python Django Tutorial Day 01

#### Installation
##### Step 01:
```
pipenv install django, mysqlclient=1.3.12
```

#### Run
##### Step 02:
```
pipenv shell
cd website
python manage.py makemigrations # create migrations file based on your model class chanegs
python manage.py migrate # migrate database 
python manage.py runserver 0.0.0.0:8080
```