# Flask App with PostgreSQL backend DB

## Introduction

This project contains a basic Flask application displaying a reading list
of books. The books are saved in a PostgreSQL database. 

## Local Development

The project contains a docker-compose.yml file to run the application and the 
database locally. Change into the ./src directory and run: 

```bash
docker compose build --build-args user_id=$(id -u) app
docker compose up -d
```


