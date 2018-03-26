# Smart Faculty Portal 

The project is a smart portal management for the faculty of any educational institute .  
# Features!

  - Interactive GUI for data updation
  - Auto - creation of the faculty web page based on the data uploaded
  - Web Scrapper to fetch data from the old faculty website based on a static template


### Requirements

* Django ( pip install django )
* Beautiful Soup ( pip install beautifulsoup4 )
* Flask
* virtualenv 
* Pillow 
* Parser 

### Installation
Install a virtaul environment to run the project 
Go the the Project Folder 
```sh
$ pip install virtualenv
$ virtualenv venv
$ cd virtualenv 
$ source /bin/activate
$ cd ..

```

For dependencies ...

```sh
$ pip install django
$ pip install beautifulsoup4
$ pip install flask
$ pip install Pillow
$ pip install lxml
```


### Deployment

Go to the SSL folder . 

```sh
cd SSL_project
cd SSL
python manage.py runserver
```

By default, it will use  port 8080 . 
To use any different port
```sh
python manage.py runserver 3128
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```


### Screenshots 
![Login](/screenshots/login.png?raw=true "Login")
![search](/screenshots/search.png?raw=true "search")
![signup](/screenshots/signup.png?raw=true "signup")
![user](/screenshots/user.png?raw=true "user")
![dashboard](/screenshots/dashboard.png?raw=true "dashboard")
![teaching](/screenshots/teaching.png?raw=true "teaching")
![Scraper](/screenshots/Scraper.png?raw=true "Scraper")
![student1](/screenshots/student1.png?raw=true "student1")
![student2](/screenshots/student2.png?raw=true "student2")


Template - https://www.creative-tim.com/product/material-dashboard

License
----
MIT



