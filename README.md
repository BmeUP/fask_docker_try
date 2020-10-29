# flask_docker_try
Try simple microservices with python-flask and docker

**Installing**

clone this repo:

``git clone https://github.com/BmeUP/fask_docker_try.git``

then change workdir:

``cd cd fask_docker_try/dockercmps_flsk``

and finaly run docker-compose:

``docker-compose up --build``

**Some Endpoints**

``http://0.0.0.0:5000/``

***return*** ``Hello, World!``

``http://0.0.0.0:5000/hell``

***return*** ``{
    "hello": "world",
    "message": "I am microservice on http://127.0.0.1:5000"
}``

``http://0.0.0.0:5353/``

***return***  ``Hello, World!``

``http://0.0.0.0:5353/ms``

***return*** ``"I am microservice on http://127.0.0.1:5000"``

