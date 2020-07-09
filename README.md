# [Flask Dashboard - Atlantis Dark Design](https://appseed.us/admin-dashboards/flask-dashboard-atlantis-dark)

> **Open-Source Admin Dashboard** coded in **Flask Framework** by **AppSeed** [Web App Generator](https://appseed.us/app-generator) - Features:

- UI Kit: **[Atlantis Dark Lite](https://www.themekita.com/atlantis-lite-bootstrap-dashboard.html?ref=appseed)** (Free version) provided by **ThemeKita**
- UI-Ready, SQLite database
- SQLAlchemy ORM
- Session-Based authentication flow (login, register)
- Forms validation
- **MIT License**
- Free support via **Github** 
- Paid Support **24/7 LIVE Support** via [Discord](https://discord.gg/fZC6hup)

 > Links
 
- [Flask Dashboard - Atlantis Dark Design](https://appseed.us/admin-dashboards/flask-dashboard-atlantis-dark) - Product page
- [Flask Dashboard Atlantis Dark Docs](https://docs.appseed.us/admin-dashboards/flask-dashboard-atlantis-dark/) - Documentation
- [Flask Dashboard Atlantis Dark Demo](https://flask-dashboard-atlantis-dark.appseed.us/login.html) - LIVE App
- More [Flask Dashboards](https://appseed.us/admin-dashboards/flask) - index hosted by **AppSeed**
- More [Admin Dashboards](https://appseed.us/admin-dashboards) - index hosted by **AppSeed**

<br />

## Want more? Go PRO!

PRO versions include **Premium UI Kits**, Lifetime updates and **24/7 LIVE Support** (via [Discord](https://discord.gg/fZC6hup))

| [Flask Gradient PRO](https://appseed.us/admin-dashboards/flask-dashboard-gradient-pro) | [Flask Dashboard Black PRO](https://appseed.us/admin-dashboards/flask-dashboard-black-pro) | [Flask Dashboard Argon PRO](https://appseed.us/admin-dashboards/flask-dashboard-argon-pro) |
| --- | --- | --- |
| [![Flask Gradient PRO](https://raw.githubusercontent.com/app-generator/flask-dashboard-gradient-pro/master/media/flask-dashboard-gradient-pro-screen.png)](https://appseed.us/admin-dashboards/flask-dashboard-gradient-pro) | [![Flask Dashboard Black PRO](https://raw.githubusercontent.com/app-generator/flask-dashboard-black-pro/master/media/flask-dashboard-black-pro-screen.png)](https://appseed.us/admin-dashboards/flask-dashboard-black-pro) | [![Flask Dashboard Argon PRO](https://raw.githubusercontent.com/app-generator/flask-dashboard-argon-pro/master/media/flask-dashboard-argon-pro-screen.png)](https://appseed.us/admin-dashboards/flask-dashboard-argon-pro)

<br />
<br />

![Flask Dashboard Atlantis Dark - Starter project coded in Flask.](https://raw.githubusercontent.com/app-generator/flask-dashboard-atlantis-dark/master/media/flask-dashboard-atlantis-dark-screen.png)

<br />

## Build from sources

```bash
$ # Clone the sources
$ git clone https://github.com/app-generator/flask-dashboard-atlantis-dark.git
$ cd flask-dashboard-atlantis-dark
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$ 
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Run the application
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the app in browser: http://127.0.0.1:5000/
```

<br />

## Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

<br />

### [Docker](https://www.docker.com/) execution
---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/app-generator/flask-dashboard-atlantis-dark.git
$ cd flask-dashboard-atlantis-dark
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5005` in your browser. The app should be up & running.

<br />

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind 0.0.0.0:8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.


<br />

### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
$ pip install waitress
```
> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
$ waitress-serve --port=8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## Credits & Links

<br />

### [Flask Framework](https://www.palletsprojects.com/p/flask/)

[Flask](/what-is/flask) is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

<br />

### [What is a dashboard](https://en.wikipedia.org/wiki/Dashboard_(business))

A dashboard is a set of pages that are easy to read and offer information to the user in real-time regarding his business. A dashboard usually consists of graphical representations of the current status and trends within an organization. Having a well-designed dashboard will give you the possibility to act and make informed decisions based on the data that your business provides - *definition provided by [Creative-Tim - Free Dashboard Templates](https://www.creative-tim.com/blog/web-design/free-dashboard-templates/?ref=appseed)*.

<br />

### [Atlantis Dark Lite](https://www.themekita.com/atlantis-lite-bootstrap-dashboard.html?ref=appseed)

**Atlantis Dark Lite** is a free bootstrap 4 admin dashboard that is beautifully and elegantly designed to display various metrics, numbers or data visualization. Atlantis Dark Lite admin dashboard has 2 layouts, many plugins and UI components to help developers create dashboards quickly and effectively so they can save development time and also help users to make the right and fast decisions based on existing data.

<br />

---
[Flask Dashboard - Atlantis Dark Design](https://appseed.us/admin-dashboards/flask-dashboard-atlantis-dark) - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).
