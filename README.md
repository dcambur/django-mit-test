# django-mit-test

## Description

**django-mit-test** is a web application built with **Django** and **Docker**, utilizing **PostgreSQL**
for data storage and **Celery** for background tasks.
It allows users to register, manage profiles, and receive welcome emails 
upon registration.

## Prerequisites

Before starting, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone git@github.com:dcambur/django-mit-test.git
cd django-mit-test
```

### 1.1 Create .env File

By default, docker-compose is configured to take it from the same path it is located in.
Below you may find the configuration the example configuration.
**Important:** SMTP settings are live and kicking, 
you don't need to change it as mail notifications will work with current preset.
(though I may close the access in the future)

```dotenv
# User Settings
DJANGO_SUPERUSER_USERNAME=some_username
DJANGO_SUPERUSER_PASSWORD=some_password
DJANGO_SUPERUSER_EMAIL=some_email@gmail.com
SECRET_KEY='django-insecure-6)@2e#++)4ggj%q9635+j&0)k&4p33^8yp3xx2u%vq+ip)+2ec'

# Celery Settings
CELERY_BROKER=redis://redis:6379/0

# Mail Settings
EMAIL_HOST=box.bitcore.cloud
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=django@bitshort.link
EMAIL_HOST_PASSWORD=RJw55P0d7iZpf7iW
DEFAULT_FROM_EMAIL="Celery <django@bitshort.link>"

# Database Settings
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=some_password
DB_HOST=postgresql
DB_PORT=5432

```

### 2. Startup docker-compose 

```bash
docker-compose up --build
```

### 3. Open The Home Page

```djangourlpath
http://localhost:8000/
```