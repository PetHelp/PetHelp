![](https://github.com/PetHelp/PetHelp/workflows/.github/workflows/frontend.yml/badge.svg)

# Pet Help Map

* [Brainstorming](https://docs.google.com/document/d/1nU1464ENjyoeEfTsOWC8a7vhgKA91a5xZyzGSqrrFsw/edit#heading=h.vwt3i2cp9nh0)
* [Entscheidungen](https://docs.google.com/document/d/1nMJlZJoSg1fzXIc-fnk-o40EpsS2XhxrF_xV5ZOt08E/edit#heading=h.x4dn4bcm6qjz)
* [Trello-Board](https://trello.com/b/5I7cLdzX/petshelpmap)
* [DEVPOST](https://devpost.com/software/1_45_c_haustiere_pethelpmap)

## Backend

### How to use docker

To use the docker image, just do:

```bash
cd backend
docker build -t pethelp-backend .
docker run --rm -p 8000:8000 pethelp-backend
```
This will run gunicorn as production server

## Frontend

### How to use docker

To use the docker image, just do:

```bash
cd frontend
docker build -t pethelp-frontend .
docker run --rm -p 8080:80 pethelp-frontend
```

## Deployment with docker-compose
First copy env.example to .env
```bash
cp env.example .env
```
Edit .env and set your preferred settings

Next compile and run:
```bash
docker-compose build
docker-compose up -d
```
