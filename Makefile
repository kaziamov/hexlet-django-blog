dev: freeze
	docker-compose up --force-recreate

freeze:
	poetry export --without-hashes --format requirements.txt > requirements.txt

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

start:
	poetry run gunicorn task_manager.wsgi

lint:
	poetry run flake8 hexlet_django_blog

rm-venv:
	rm -rf `poetry env info -p`