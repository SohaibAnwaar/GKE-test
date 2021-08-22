# Story

This git is designed to test the GCP cloud services

1. Load Balancing 
    1. Regional
    2. Zonal
    3. Global

2. Kubernetes Engine
    1. Deployment of clusters in different zones.

<br>

## Installation
This script includes a flask endpoint which gives you the 

1. IP
2. org
3. city
4. country
5. region

of the server on which request is processed.


### Download the script
<br>

Commands required to start the script
<br>

```
conda create -n docker_test python=3.6 flask
conda activate docker_test
python test.py
```

<br>

Now hit your localhost on port 5000 like this https://localhost:5000

<br>

You will get the answer like this

```
request completed 101.53.234.28 AS9541 Cyber Internet Services (Pvt) Ltd. Lahore PK Punjab
```

**Sucess**

<br>


## Local Kubernetes Testing

For local Kubernetes testing, you have to make a docker image of it and upload it into your docker hub repo. For testing purposes, you can use mine.

```
docker pull sohaibanwaar/gcpdockertesting

docker container run -it -p 5000:5000 --name kubetest sohaibanwaar/gcpdockertesting
```

Now hit the same URL above you will get the same answer.

**tada you succeed once again**



