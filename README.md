# How to use

1. install pipenv
```
$ brew install pipenv
```

2. clone this repository and cd project
```
$ git clone https://github.com/klein-mask/instagram-likes-tool.git

$ cd instagram-likes-tool
```

3. create virtual environment by pipenv 
```
$ pipenv sync
```

4. run server
```
$ cd core

$ pipenv run python manage.py runserver
```

5. access application
```
http://127.0.0.1:8000/app/index/
```