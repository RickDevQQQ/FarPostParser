# Чекпорт
## Докер: сборка и запуск контейнера
```sh
sudo docker compose up --force-recreate -V
```
## Докер: остановка контейнера
```sh
sudo docker compose down
```
## Докер: удаление всех незапущенных контейнеров и образов
```sh
sudo docker system prune -a
```
## Докер: удаление всех volume
```sh
sudo docker volume prune -a
```
## Докер: список всех образов
```sh
sudo docker image ls -a
```
## Докер: список всех контейнеров
```sh
sudo docker container ls -a
```
## Докер: посмотреть файлы внутри образа
```sh
sudo docker run -it checkport_fastapi_fastapi  sh
# Для выхода
exit
```
## Докер: посмотреть файлы внутри запущенного контейнера
```sh
sudo docker exec -it checkport_fastapi_fastapi_1  sh
```
## Посмотреть открытые порты на хосте
```sh
sudo lsof -i -P -n | grep LISTEN
```
## Запуск postgresql на хосте
```sh
sudo service postgresql start
```
## Остановка postgresql на хосте
```sh
sudo service postgresql stop
```
## Запуск uvicorn на хосте
```sh
sh run_app.sh
```
## Остановка uvicorn на хосте
```sh
sudo sh kill_app.sh
```