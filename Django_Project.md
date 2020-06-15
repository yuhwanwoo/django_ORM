## Django Project

------

### 프로젝트 생성

* project Name : mysite
* App Name : 



### 페이지 생성

1. index page
   * /index/ : 전체 게시글 목록을 보여 줄 페이지











* terminal

```bash
student@M16015 MINGW64 ~/Desktop/django_ORM/mysite
$ python manage.py makemigrations  ## 지정해서 밑에 migrate하면 된대
Migrations for 'articles':
  articles\migrations\0001_initial.py
    - Create model Article

student@M16015 MINGW64 ~/Desktop/django_ORM/mysite
$ python manage.py migrate articles  #스키마 생성
Operations to perform:
  Apply all migrations: articles
Running migrations:
  Applying articles.0001_initial... OK

```





* db접근

```bash
student@M16015 MINGW64 ~/Desktop/django_ORM/mysite
$ python manage.py shell
```

