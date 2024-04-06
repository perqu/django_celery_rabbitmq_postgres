## Simple Django project with Celery, RabbitMQ, Flower and Postgres

Example of implementations a simple Django app with Celery tasks, RabbitMQ, Flower UI and Postgress DB.

## Celery tasks

1. `PeriodicTask (every 30 seconds)`
2. `SimpleTask1` - queue1
3. `SimpleTask2` - queue2

## Docker-compose configuration

- `app`: Django app - Web server + basic UI with buttons to run the tasks
- `worker1`: Celery worker/queue1 - worker1 for SimpleTask1
- `worker2`: Celery worker/queue2 - worker2 for SimpleTask2
- `worker3`: Celery worker for periodic task
- `rabbitmq`: RabbitMQ broker - Celery message broker
- `flower`: Flower UI - Celery monitoring tool
- `postgres`: RDBMS

## How to run the project

1. Clone the repository
2. Install docker
3. Run `docker compose build`
4. Run `docker compose up`
5. Open http://0.0.0.0:8888 in your browser to see the Swagger UI
   - Click on the button 1 to run the SimpleTask1
   - Click on the button 2 to run the SimpleTask2
6. Open http://0.0.0.0:5556 in your browser to see the Flower UI
