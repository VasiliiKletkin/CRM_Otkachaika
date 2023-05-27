# Otkachaika CRM

This project was created for the management of Autumn services of the Otkachayka company.Project allows you to receive up-to-date information on orders, manage drivers, and monitor analytics.

The goal of the project is to automate the process of ossenization services for easier scaling.

## Stack

* Postgres
* Django
* PytelegramBot
* Rabbit MQ
* Celery

## Start project with `docker-compose`

$ cp .env.example .env.local
$ docker-compose up -d --build

Exec commands for docker containers:

```bash
# load database dump from staging
$ make dcreatedb
$ make dloaddump
# dump database from docker container
$ make dcreatedump
# delete database from docker container
$ make ddeletedb

# make migrations && migrate
$ make dmigr
```
