# GeoAPI

## Technology

- Django
- django rest framework
- PostgreSQL
- requests
- gunicorn
- nginx
- JWT

The reason of chosen technology is that they have good community support and official documentation. Additionaly these technologies are used in many companies around the world.

## Prequesites

- Due to compose file format 3.8 (Required Docker Engine release 19.03.0+)

## Development Setup

1. Create your own version of `env.dev` by simply copying contents of `env.dev.example`.

2. In root directory run `docker-compose -f docker-compose.yml up -d` to build the app.

3. After build run `docker-compose -f docker-compose.yml exec web python manage.py migrate --no-input` to add migrations into database.

## Production Setup

1. Create your own version of `env.prod` by simply copying contents of `env.prod.example`.

2. Create your own version of `env.prod.db` by simply copying contents of `env.prod.db.example`.

3. In root directory run `docker-compose -f docker-compose.prod.yml up -d` to build the app.

4. After build run `docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --no-input` to add migrations into database.

5. Run `docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic` to add static files.

## Last Step

API is available on `/api/`, e.g if you run it on `http://localhost:8000` it's `http://localhost:8000/api/`. 