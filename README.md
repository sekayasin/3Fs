# 3Fs - Fast-Food-Fast

3Fs (Fast-Food-Fast) is a food delivery service app for a restaurant

[![Build Status](https://travis-ci.org/sekayasin/3Fs.svg?branch=3fs-react-fe)](https://travis-ci.org/sekayasin/3Fs)
[![Coverage Status](https://coveralls.io/repos/github/sekayasin/3Fs/badge.svg?branch=3fs-react-fe)](https://coveralls.io/github/sekayasin/3Fs?branch=3fs-react-fe)
[![Maintainability](https://api.codeclimate.com/v1/badges/265ca6d8e55d6437cffa/maintainability)](https://codeclimate.com/github/sekayasin/3Fs/maintainability)

###### :page_facing_up: NOTE

3Fs Project is a living playground project that I use to quickly aid my learning of any framework/language i wish to learn.

## Dockerizing a React app and Deploying the app to a Kubernetes Cluster

Using Containers for Deployment

---

##### Dockerizing 3Fs app and deploy it to K8s Cluster on GCP

---

[Screencast](https://drive.google.com/open?id=1YF1_AI-vUlPt8c2iMQ42hjvn3xW_QlmT) showing how the app is dockerized and deployed to K8s cluster on GCP

Using Docker - a popular containerization tool

1. A Docker image of the app is created using Docker multi-stage builds, this will result in building a leaner image, which leads to faster deployment and a more efficient containerization in production.

Here is our Dockerfile

```
## STAGE 1: BUILD ##
FROM node:lts-alpine as build

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

RUN npm install yarn -g

COPY package.json /usr/src/app/package.json

RUN yarn

COPY . /usr/src/app

RUN yarn build

## STAGE 2: PRODUCTION ##

FROM nginx:1.14.2-alpine

COPY --from=build /usr/src/app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

```

STAGE 1: The Build

We extend our image from a Node.js LTS alpine base image and label it as `build`
COPY `package.json` file at first, rather than the whole working directory which allows us to take advantage of Docker's cache layers
Install all our dependencies using `yarn`
COPY our app sources and build it with `yarn build`. Our app is now ready for production

STAGE 2: The Production

Since all we need to run the app is a web server. We start stage two by extending the Nginx base image based on Alpine, this will lead to slimmer image in general
COPY over the contents of dist directory to Nginx default document root directory. Docker allows us to reference the results of the first stage by the label we provided: `build`
Nginx will serve on port 80, we expose it - We map this port to a port on the host running the container
Finally we define default command which Docker will run when executing the container.

Build and Run the Docker Image
Having everything in place, we can build and tag the image by running `docker build` within your projects directory.

```
docker build -t 3fs-demo .

docker image ls
REPOSITORY                                             TAG                 IMAGE ID            CREATED             SIZE
3fs-demo                                               latest              5f80284b4aec        12 hours ago        17MB
```

To run our freshly baked image, we call `docker run` command. Docker run the container and map the internal port which is used by Nginx to serve our project to port 3000 of the host system our Docker instance is running on.

```
docker run -p 3000:80 3fs-demo
```

Hang-on. We want to deploy our app to a Kubernetes cluster on GCP
We will need to Push our docker image to container registry on GCP

1. To push any local image to Container Registry, you need to first tag it with the registry name and then push the image

```
docker tag 3fs-demo eu.gcr.io/hybrid-ridge-235016/3fs-demo

docker push eu.gcr.io/hybrid-ridge-235016/3fs-demo
```

`eu.gcr.io` specifies the region of the registry's storage, hosts the image in the European Union
`hybrid-ridge-235016` is my GCP Project ID
`3fs-demo` the source image

Login to GCP cloud console and deploy the app to K8s cluster

```
gcloud config set project <projectID>
gcloud config set compute/zone <zone>

# create a cluster
gcloud container clusters create <myCluster>

# fetch cluster authentication credentials
gcloud container clusters get-credentials <myCluster>

# run your first deployment
kubectl run fastfood-demo --image eu.gcr.io/<projectID/image> --port 80

# expose the service
kubectl expose deployment fastfood-demo --type LoadBalancer
```

App is deployed on K8s cluster. Can be reached using this IP: http://35.246.29.36/

---

## 3Fs Web App - Reactify Frontend (Reactjs)

Setting up 3Fs Frontend Environment with Reactjs - with Webpack and Babel

---

##### 3Fs React Frontend Project Setup

---

1. Clone the Repository
   `https://github.com/sekayasin/3Fs.git`

2. Navigate to the application directory
   `cd 3fs-react-fe`

3. install all dependencies
   `yarn install`

4. Run the application
   `yarn start`

5. Run 3Fs React Web App locally in the browser
   `http://localhost:3000`

---

###### 3Fs Reactify Frontend Available Endpoints working

| URL     | Methods               | Functionality     |
| ------- | --------------------- | ----------------- |
| sign-up | **POST** /auth/signup | `signs up a user` |
| log-in  | **POST** /auth/signin | `Logs in a user`  |

---

###### :microscope: 3Fs Reactify Frontend - Run Tests

- [x] Tests for components
- [x] Tests for reducers
- [x] Tests for actions

- command to run tests:
  `yarn test -u`

- command to run tests with coverage:
  `yarn test -u --coverage`

---

###### 3Fs Reactify Frontend Demo

> The application is deployed on Heroku [here](https://sekayasin-3fs-react-webapp.herokuapp.com/)

:microscope: Test users

> Test user

    ` username: user.yasin, password: user.yasin123 `

> Test admin user

    ` username: admin.yasin, password: admin.yasin123 `

---

## 3Fs Web App - Vanila Js

3Fs Web App is hosted on Heroku [here](https://sekayasin-3fs-webapp.herokuapp.com)

## 3Fs API v2

3Fs API v2 is hosted on Heroku [here](https://sekayasin-3fs-apiv2.herokuapp.com)

## 3Fs API v1

3Fs API v1 is hosted on Heroku <a href="https://sekayasin-3fs-api.herokuapp.com/">here</a>

## Project Progress managed with PivotalTracker

You can check on the project progress board <a href="https://www.pivotaltracker.com/n/projects/2195804">here</a>

## 3Fs Demo UI Templates on GitHub Pages

3Fs Demo Website hosted on GitHub pages <a href="https://sekayasin.github.io/3Fs/UI">here</a>

### For 3Fs Admin only - UI Templates

3Fs Admin Login URL can be found <a href="https://sekayasin.github.io/3Fs/UI/admin.html">here</a>

The 3Fs API will serve two parties, the 3fs client(customer) and the administrator (admin).\
The client will use the api to place an order, query his/her latest orders, and also query a specific order.\
The Admin will use the api to update client's status order, update menu available at 3fs, query available orders,\
specfic order, remove completed orders.

The table below shows the 3Fs api v1 endpoints

| Endpoint                          | User   | Functionality                                                    |
| --------------------------------- | ------ | ---------------------------------------------------------------- |
| GET /api/v1/client/menu           | client | The client can check the available menu at 3fs takeaway          |
| POST /api/v1/orders               | client | The client can place a new order                                 |
| POST /api/v1/menu                 | admin  | The admin to add a food-item and its price on the available menu |
| GET /api/v1/client/orders/orderID | client | The client can get his/her order by orderID                      |
| GET /api/v1/orders                | admin  | The admin can get all the available orders                       |
| GET /api/v1/orders/orderID        | admin  | The admin can get a specific order                               |
| PUT /api/v1/orders/orderID        | admin  | The admin can update status of a specific order                  |
| DELETE /api/v1/orders/orderID     | admin  | The admin can remove a completed order                           |

The table shows the 3Fs api v2 endpoints

| Endpoint               | User  | Functionality                                    |
| ---------------------- | ----- | ------------------------------------------------ |
| POST /auth/signup      | users | Register a user                                  |
| post /auth/login       | users | Login a user                                     |
| POST /menu             | Admin | Only the Admin to add a meal option to the menu  |
| GET /menu              | User  | Users should be able to get the available menu   |
| POST /users/orders     | user  | Place an order for food                          |
| GET /orders            | Admin | Only Admin user should be able to get all orders |
| GET /users/orders      | User  | Get the order history for a specific user        |
| GET /orders/OrderID    | Admin | The admin to get a specific order                |
| PUT /orders/OrderID    | Admin | The admin to update the status of an order       |
| DELETE /orders/OrderID | Admin | The admin to remove a completed order            |

## Project Overview

### Technologies Used

#### 3Fs Website

1. Project is Designed using HTML5/CSS3/Js
2. Background images and images used are embedded using unsplash API, <a href="https://source.unsplash.com/">read more</a> about unsplash API.
3. ionicons have been used to provide icon fonts, <a href="https://ionicons.com/">read more</a> about ionicons.
4. GoogleFonts have been used to make the typography beautiful and great, <a href="https://fonts.google.com/">read more</a> about GoogleFonts.

#### 3Fs API v1

##### Installation

In order to run the api application, follow these steps

1. Start by cloning the api repo locally to your machine

```
$ git clone https://github.com/sekayasin/3Fs.git
$ cd 3Fs
$ git checkout dev
```

2. Project requires that you have python 3 installed. Tested on python 3.6.5

- Project has been tested on python 3.6.5 in a virtual environement using Virtualenv and Virtualenvwrapper
- Download and Install python 3.6 or above [here](https://www.python.org/downloads/)

```
$ pip install virtualenv
$ pip install virtualenvwrapper
```

- Or You can work with the lightweight virtual environmnets introduced in python3.4

```
$ python3 -m venv virtualenvironment_name
```

- Activate your virtual environment

```
$ source ~/3Fs/virtualenvironment_name/bin/activate
```

- Now install the requirements.txt file in 3Fs

```
$ pip install -r requirements.txt
```

- Set flask environment variable
- cloned 3Fs has a .flaskenv file... You should be good to go
- UNIX

```
$ export FLASK_APP=run.py
```

- Run the app

```
flask run
```

##### Usage

For api v1 , I have recorded a screencast on how to test the api endpoints on YouTube [here](https://www.youtube.com/watch?v=lGi0FNqr_Ps)

#### 3Fs API v2

##### Installation

In order to run the api v2 application, follow these steps

1. Start by cloning the api repo locally to your machine

```
$ git clone https://github.com/sekayasin/3Fs.git
$ cd 3Fs
$ git checkout develop
```

2. Continue with steps 2 above for api v1

#### 3Fs Web App

3Fs Web App is hosted on Heroku [here](https://sekayasin-3fs-webapp.herokuapp.com)

This implements the use of the JavaScript Fetch API to perform AJAX

## Andela Uganda Cohort 12

3Fs project is a Series of Challenge project requirement for **Cohort 12 Andela Uganda** Bootcampers

1. Challenge 1 - Frontend (HTML/CSS) - Fast-Food-Fast Website
2. Challenge 2 - API Design - Fast-Food-Fast API v1 - Data is persisted to a Data-structure
3. Challenge 3 - API Design - Fast-Food-Fast API v2 - Add more API endpoints and Data is persisted to a Postgres DB
4. Challenge 4 - JS to Power the Frontend - Use JavaScript Fetch API to Perform AJAX to supercharge your Frontend.

### Contact information for thatGuy! our Awesome Developer!

- Name: **Sekabira Yasin** , call me _sekayasin_
- ping me: sekayasin@gmail.com
- I hang-out on GitHub, u can <a href="https://github.com/sekayasin">fork me</a> or on my tinkering <a href="https://sekayasin.me/">Portfolio</a>
- If u would like to follow me on Twitter, my username is _@sekayasin9_
