.PHONY: help
help:
	@echo "--------------- SituationRoom ---------------"
	@echo "make help                            -Display this list"
	@echo "make build                           -Build docker container for local use"
	@echo "make migrate                         -Run Django migrations"
	@echo "make makemigrations app={app_name}   -Create migrations for an app"
	@echo "make app name={app_name}             -Creates a new django app" 
	@echo "make shell_plus		                -Runs a shell in the container"
	@echo "make logs		                    -Show the django logs"


WEB_CONTAINER_ID := $(shell docker-compose ps -q web)

.PHONY: build
build: 
	docker-compose build

.PHONY: app
app:
	docker-compose run --rm web python manage.py startapp $(name)

.PHONY: makemigrations
makemigrations:
	docker-compose run --rm web python manage.py makemigrations $(app)

.PHONY: migrate
migrate:
	docker-compose run --rm web python manage.py migrate

.PHONY: shell_plus
shell_plus:
	docker-compose exec web python manage.py shell_plus --ipython

.PHONY: logs
logs:
	docker-compose logs -f $(WEB_CONTAINER_ID)