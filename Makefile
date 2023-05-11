dev: freeze
	docker-compose up --force-recreate

freeze:
	poetry export --without-hashes --format requirements.txt > requirements.txt

up:
	docker-compose up

stop:
	docker-compose stop && docker-compose rm && sudo rm -rf pgdata/

start:
	poetry run gunicorn hexlet_django_blog.wsgi --bind 0.0.0.0:8000

start-server:
	gunicorn hexlet_django_blog.wsgi --bind 0.0.0.0

migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate

shell:
	poetry run python manage.py shell

superuser:
	poetry run python manage.py createsuperuser

deploy:
	railway up

lint:
	poetry run flake8 hexlet_django_blog

rm-venv:
	rm -rf `poetry env info -p`

start-db:
	docker-compose -f docker-compose.db.yml up