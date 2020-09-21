# Board - Part1

## Why Django?

Django is a Web framework written in Python. A Web framework is a software that supports the development of dynamic Web sites, applications, and services. It provides a set of tools and functionalities that solves many common problems associated with Web development, such as security features, database access, sessions, template processing, URL routing, internationalization, localization, and much more.

Using a Web framework, such as Django, enables us to develop secure and reliable Web applications very quickly in a standardized way, without having to reinvent the wheel.
So, what’s so special about Django? For starters, it’s a Python Web framework, which means you can benefit from wide a range of open source libraries out there. The [Python Package Index](https://pypi.python.org/pypi) repository hosts over **116K** packages (as per 6 of Sep. 2017). If you need to solve a specific problem, the chances are someone has already implemented a library for it.

Django is one of the most popular Web frameworks written in Python. It’s definitely the most complete, offering a wide range of features out-of-the-box, such as a standalone Web server for development and testing, caching, middleware system, ORM, template engine, form processing, interface with Python’s unit testing tools. Django also comes with *battery included*, offering built-in applications such as an authentication system, an administrative interface with automatically generated pages for CRUD operations, generation of syndication feeds (RSS/Atom), sitemaps. There’s even a Geographic Information System (GIS) framework built within Django.

The development of Django is supported by the [Django Software Foundation](https://www.djangoproject.com/foundation/), and it’s sponsored by companies like JetBrains and Instagram. Django has also been around for quite some time now. It’s under active development for more than 12 years now, proving to be a mature, reliable and secure Web framework.

**Who’s Using Django?**

It’s good to know who is using Django out there, so to have an idea what you can do with it. Among the biggest Web sites using Django we have: [Instagram](https://instagram.com/),[Disqus](https://disqus.com/), [Mozilla](https://www.mozilla.org/), [Bitbucket](https://bitbucket.org/), [Last.fm](https://www.last.fm/), [National Geographic](http://www.nationalgeographic.com/).

For more examples you can see the [Django Sites](https://www.djangosites.org/) database, they offer a list of over **5K** Django-powered Web sites.

By the way, last year, in the Django Under The Hood 2016 conference, Carl Meyer, a Django core developer, and Instagram employee, gave a talk on [how Instagram use Django at scale](https://www.youtube.com/watch?v=lx5WQjXLlq8) and how it supported their growth. It’s a one hour talk, but if you are interested in learning more, it was an entertaining talk.

----------

**Installation**
The first thing we need to do is install some programs on our machine so to be able to start playing with Django. The basic setup consists of installing **Python**, **Virtualenv**, and **Django**.

Using virtual environments is not mandatory, but it’s highly recommended. If you are just getting started, it’s better to start with the right foot.

When developing Web sites or Web projects with Django, it’s very common to have to install external libraries to support the development. Using virtual environments, each project you develop will have its isolated environment. So the dependencies won’t clash. It also allows you to maintain in your local machine projects that run on different Django versions.

## Installing Virtualenv

For the next step, we are going to use **pip**, a tool to manage and install Python packages, to install **virtualenv**.


    sudo pip3 install virtualenv


![pip3 install virtualenv](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/mac/pip-virtualenv.png)


So far the installations that we performed was system-wide. From now on, everything we install, including Django itself, will be installed inside a Virtual Environment.
Think of it like this: for each Django project you start, you will first create a Virtual Environment for it. It’s like having a sandbox for each Django project. So you can play around, install packages, uninstall packages without breaking anything.
I like to create a folder named **Development** on my personal computer. Then, I use it to organize all my projects and websites. But you can follow the next steps creating the directories wherever it feels right for you.
Usually, I start by creating a new folder with the project name inside my **Development** folder. Since this is going to be our very first project, we don’t need to pick a fancy name or anything. For now, we can call it **myproject**.


    mkdir myproject
    cd myproject


![Create myproject folder](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/mac/myproject.png)


This folder is the higher level directory that will store all the files and things related to our Django project, including its virtual environment.
So let’s start by creating our very first virtual environment and installing Django.
Inside the **myproject** folder:


    virtualenv venv -p python3



![Virtualenv](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/mac/venv.png)


Our virtual environment is created. Now before we start using it, we need to activate:


    source venv/bin/activate

You will know it worked if you see **(venv)** in front of the command line, like this:

![Virtualenv activate](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/mac/activate.png)


Let’s try to understand what happened here. We created a special folder named **venv**. It contains a copy of Python inside this folder. After we activated the **venv**environment, when we run the `python` command, it will use our local copy, stored inside **venv**, instead of the other one we installed earlier.
Another important thing is that the **pip** program is already installed as well, and when we use it to install a Python package, like Django, it will be installed *inside*the **venv** environment.
Note that when we have the **venv** activated, we will use the command `python`(instead of `python3`) to refer to Python 3.6.2, and just `pip` (instead of `pip3`) to install packages.
By the way, to deactivate the **venv** run the command below:
But let’s keep it activated for the next steps.
**Installing Django 1.11.4**
It’s very straightforward. Now that we have the **venv** activated, run the following command to install Django:


    pip install django



![pip install django](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/mac/pip-django.png)


We are all set up now!


## Starting a New Project

To start a new Django project, run the command below:


    django-admin startproject myproject

The command-line utility **django-admin** is automatically installed with Django.
After we run the command above, it will generate the base folder structure for a Django project.
Right now, our **myproject** directory looks like this:


    myproject/                  <-- higher level folder
     |-- myproject/             <-- django project folder
     |    |-- myproject/
     |    |    |-- __init__.py
     |    |    |-- settings.py
     |    |    |-- urls.py
     |    |    |-- wsgi.py
     |    +-- manage.py
     +-- venv/                  <-- virtual environment folder

Our initial project structure is composed of five files:

- **manage.py**: a shortcut to use the **django-admin** command-line utility. It’s used to run management commands related to our project. We will use it to run the development server, run tests, create migrations and much more.
- **__init__.py**: this empty file tells Python that this folder is a Python package.
- **settings.py**: this file contains all the project’s configuration. We will refer to this file all the time!
- **urls.py**: this file is responsible for mapping the routes and paths in our project. For example, if you want to show something in the URL `/about/`, you have to map it here first.
- **wsgi.py**: this file is a simple gateway interface used for deployment. You don’t have to bother about it. Just let it be for now.

Django comes with a simple web server installed. It’s very convenient during the development, so we don’t have to install anything else to run the project locally. We can test it by executing the command:


    python manage.py runserver

For now, you can ignore the migration errors; we will get to that later.
Now open the following URL in a Web browser: **http://127.0.0.1:8000** and you should see the following page:

![It worked!](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/it-worked.png)


Hit Control + C to stop the development server.

----------

**Django Apps**
In the Django philosophy we have two important concepts:

- **app**: is a Web application that does something. An app usually is composed of a set of models (database tables), views, templates, tests.
- **project**: is a collection of configurations and apps. One project can be composed of multiple apps, or a single app.

It’s important to note that you can’t run a Django **app** without a **project**. Simple websites like a blog can be written entirely inside a single app, which could be named **blog** or **weblog** for example.

It’s a way to organize the source code. In the beginning, it’s not very trivial to determine what is an app or what is not. How to organize the code and so on. But don’t worry much about that right now! Let’s first get comfortable with Django’s API and the fundamentals.
Alright! So, to illustrate let’s create a simple Web Forum or Discussion Board. To create our first app, go to the directory where the **manage.py** file is and executes the following command:


    django-admin startapp boards

Notice that we used the command **startapp** this time.
This will give us the following directory structure:


    myproject/
     |-- myproject/
     |    |-- boards/                <-- our new django app!
     |    |    |-- migrations/
     |    |    |    +-- __init__.py
     |    |    |-- __init__.py
     |    |    |-- admin.py
     |    |    |-- apps.py
     |    |    |-- models.py
     |    |    |-- tests.py
     |    |    +-- views.py
     |    |-- myproject/
     |    |    |-- __init__.py
     |    |    |-- settings.py
     |    |    |-- urls.py
     |    |    |-- wsgi.py
     |    +-- manage.py
     +-- venv/


So, let’s first explore what each file does:

- **migrations/**: here Django store some files to keep track of the changes you create in the **models.py** file, so to keep the database and the **models.py** synchronized.
- **admin.py**: this is a configuration file for a built-in Django app called **Django Admin**.
- **apps.py**: this is a configuration file of the app itself.
- **models.py**: here is where we define the entities of our Web application. The models are translated automatically by Django into database tables.
- **tests.py**: this file is used to write unit tests for the app.
- **views.py**: this is the file where we handle the request/response cycle of our Web application.

Now that we created our first app, let’s configure our project to *use* it.
To do that, open the **settings.py** and try to find the `INSTALLED_APPS` variable:
**settings.py**


    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

As you can see, Django already come with 6 built-in apps installed. They offer common functionalities that most Web applications need, like authentication, sessions, static files management (images, javascripts, css, etc.) and so on.
We will explore those apps as we progress in this tutorial series. But for now, let them be and just add our **boards** app to the list of `INSTALLED_APPS`:


    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    
        'boards',
    ]

Using the analogy of the square and circles from the previous comic, the yellow circle would be our **boards** app, and the **django.contrib.admin**, **django.contrib.auth**, etc, would be the red circles.

----------

**Hello, World!**

Let’s write our first **view**. We will explore it in great detail in the next tutorial. But for now, let’s just experiment how it looks like to create a new page with Django.
Open the **views.py** file inside the **boards** app, and add the following code:
**views.py**


    from django.http import HttpResponse
    
    def home(request):
        return HttpResponse('Hello, World!')

Views are Python functions that receive an `HttpRequest` object and returns an `HttpResponse` object. Receive a *request* as a parameter and returns a *response* as a result. That’s the flow you have to keep in mind!
So, here we defined a simple view called **home** which simply returns a message saying **Hello, World!**.
Now we have to tell Django *when* to serve this view. It’s done inside the **urls.py**file:
**urls.py**


    from django.conf.urls import url
    from django.contrib import admin
    
    from boards import views
    
    urlpatterns = [
        url(r'^$', views.home, name='home'),
        url(r'^admin/', admin.site.urls),
    ]


If you compare the snippet above with your **urls.py** file, you will notice I added the following new line: `url(r'^$', views.home, name='home')` and imported the **views** module from our app **boards** using `from boards import views`.
As I mentioned before, we will explore those concepts in great detail later on.
But for now, Django works with **regex** to match the requested URL. For our **home** view, I’m using the `^$` regex, which will match an empty path, which is the homepage (this url: **http://127.0.0.1:8000**). If I wanted to match the URL**http://127.0.0.1:8000/homepage/**, my url would be: `url(r'^homepage/$', views.home, name='home')`.
Let’s see what happen:


    python manage.py runserver

In a Web browser, open the http://127.0.0.1:8000 URL:

![Hello, World!](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/hello-world.png)


That’s it! You just created your very first view.

----------


