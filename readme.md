# commands

db:
`docker-compose exec web python manage.py flush --no-input`
`docker-compose exec web python manage.py migrate`

collect static:
`$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear`

start dev
```
docker-compose up -d
```

start prod
```
$ docker-compose -f docker-compose.prod.yml down -v
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

stop dev
```
docker-compose down -v
```

stop prod
```
docker-compose -f docker-compose.prod.yml down -v
```