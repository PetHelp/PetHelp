# Pet Help Map

* [Brainstorming](https://docs.google.com/document/d/1nU1464ENjyoeEfTsOWC8a7vhgKA91a5xZyzGSqrrFsw/edit#heading=h.vwt3i2cp9nh0)
* [Entscheidungen](https://docs.google.com/document/d/1nMJlZJoSg1fzXIc-fnk-o40EpsS2XhxrF_xV5ZOt08E/edit#heading=h.x4dn4bcm6qjz)
* [Trello-Board](https://trello.com/b/5I7cLdzX/petshelpmap)

## Backend
### How to use docker
To use the docker image, just do:

```bash
cd backend
docker build -t pethelp-backend .
docker run -it --rm -v ${PWD}:/app -p 8000:8000 pethelp-backend
```
This will run python3 manage.py runserver

If you need to do other manage.py commands (e.g. migrate) do:

```bash
docker run --rm -v ${PWD}:/app pethelp-backend migrate
```
