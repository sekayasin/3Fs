# 3Fs - Fast-Food-Fast
3Fs (Fast-Food-Fast) is a food delivery service app for a restaurant

[![Build Status](https://travis-ci.com/sekayasin/3Fs.svg?branch=develop)](https://travis-ci.com/sekayasin/3Fs)
[![Coverage Status](https://coveralls.io/repos/github/sekayasin/3Fs/badge.svg?branch=develop)](https://coveralls.io/github/sekayasin/3Fs?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/265ca6d8e55d6437cffa/maintainability)](https://codeclimate.com/github/sekayasin/3Fs/maintainability)

## 3Fs Demo webiste on GitHub Pages
3Fs Demo Website hosted on GitHub pages <a href="https://sekayasin.github.io/3Fs/UI">here</a>
### For 3Fs Admin only
3Fs Admin Login URL can be found <a href="https://sekayasin.github.io/3Fs/UI/admin.html">here</a>

## Project Progress managed with PivotalTracker 
You can check on the project progress board <a href="https://www.pivotaltracker.com/n/projects/2195804">here</a>

## 3Fs API v1
3Fs API v1 is hosted on Heroku <a href="https://sekayasin-3fs-api.herokuapp.com/">here</a>

## 3Fs API v2
3Fs API v2 is hosted on Heroku [here](https://sekayasin-3fs-apiv2.herokuapp.com)

The 3Fs API will serve two parties, the 3fs client(customer) and the administrator (admin).\
The client will use the api to place an order, query his/her latest orders, and also query a specific order.\
The Admin will use the api to update client's status order, update menu available at 3fs, query available orders,\
specfic order, remove completed orders.
 
The table below shows the 3Fs api v1 endpoints

| Endpoint | User | Functionality |
| --- | --- | --- |
| GET /api/v1/client/menu | client | The client can check the available menu at 3fs takeaway |
| POST /api/v1/orders | client | The client can place a new order |
| POST /api/v1/menu | admin | The admin to add a food-item and its price on the available menu |
| GET /api/v1/client/orders/orderID | client | The client can get his/her order by orderID |
| GET /api/v1/orders | admin | The admin can get all the available orders |
| GET /api/v1/orders/orderID | admin | The admin can get a specific order |
| PUT /api/v1/orders/orderID | admin | The admin can update status of a specific order |
| DELETE /api/v1/orders/orderID | admin | The admin can remove a completed order |

The table shows the 3Fs api v2 endpoints

| Endpoint | User | Functionality |
| --- | --- | --- |
| POST /auth/signup | users | Register a user |
| post /auth/login | users | Login a user |
| POST /menu | Admin | Only the Admin to add a meal option to the menu |
| GET /menu | User | Users should be able to get the available menu |
| POST /users/orders | user | Place an order for food |
| GET /orders | Admin | Only Admin user should be able to get all orders |
| GET /users/orders | User | Get the order history for a specific user |
| GET /orders/OrderID | Admin | The admin to get a specific order |
| PUT /orders/OrderID | Admin | The admin to update the status of an order |
| DELETE /orders/OrderID | Admin | The admin to remove a completed order |
   
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

## Andela Uganda Cohort 12
3Fs project is a Challenge project requirement for **Cohort 12 Andela Uganda** Bootcampers
1. Challenge 1 - Frontend (HTML/CSS) - Fast-Food-Fast Website
2. Challenge 2 - API Design - Fast-Food-Fast API v1 - Data is persisted to a Data-structure
3. Challenge 3 - API Design - Fast-Food-Fast API v2 - Add more API endpoints and Data is persisted to a Postgres DB

### Contact information for thatGuy! our Awesome Developer!
- Name: **Sekabira Yasin** , call me *sekayasin*
- ping me: sekayasin@gmail.com
- I hang-out on GitHub, u can <a href="https://github.com/sekayasin">fork me</a> or on my tinkering <a href="https://sekayasin.me/">Portfolio</a>
- If u would like to follow me on Twitter, my username is *@sekayasin9*
