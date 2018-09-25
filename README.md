# 3Fs - Fast-Food-Fast
3Fs (Fast-Food-Fast) is a food delivery service app for a restaurant\

[![Build Status](https://travis-ci.com/sekayasin/3Fs.svg?branch=dev)](https://travis-ci.com/sekayasin/3Fs)
[![Coverage Status](https://coveralls.io/repos/github/sekayasin/3Fs/badge.svg?branch=dev)](https://coveralls.io/github/sekayasin/3Fs?branch=dev)
[![Maintainability](https://api.codeclimate.com/v1/badges/265ca6d8e55d6437cffa/maintainability)](https://codeclimate.com/github/sekayasin/3Fs/maintainability)

## 3Fs Demo webiste on GitHub Pages
3Fs Demo Website hosted on GitHub pages <a href="https://sekayasin.github.io/3Fs/UI">here</a>
### For 3Fs Admin only
3Fs Admin Login URL can be found <a href="https://sekayasin.github.io/3Fs/UI/admin.html">here</a>

## Project Progress managed with PivotalTracker 
You can check on the project progress board <a href="https://www.pivotaltracker.com/n/projects/2195804">here</a>

## 3Fs API
3Fs API is hosted on Heroku <a href="https://sekayasin-3fs-api.herokuapp.com/">here</a>\

The 3Fs API will serve two parties, the 3fs client(customer) and the administrator (admin).\
The client will use the api to place an order, query his/her latest orders, and also query a specific order.\
The Admin will use the api to update client's status order, update menu available at 3fs, query available orders,\
specfic order, remove completed orders.\
 
The table shows the api endpoints\
| Endpoint | User | Functionality |
| --- | --- | --- |
| GET /api/v1/client/menu | client | The client can check the available menu at 3fs takeaway |
| POST /api/v1/orders | client | The client can place a new order |
| GET /api/v1/client/orders/<clientUsername> | client | The client can get his/her latest orders |
| GET /api/v1/client/orders/<orderId> | client | The client can get his/her order by orderID |
| GET /api/v1/orders | admin | The admin can get all the available orders |
| GET /api/v1/orders/<orderID> | admin | The admin can get a specific order |
| PUT /api/v1/orders/<orderID> | admin | The admin can update status of a specific order |
| DELETE /api/v1/orders/<orderID> | admin | The admin can remove a completed order |
   
## Project Overview
### Technologies Used
#### 3Fs Website
1. Project is Designed using HTML5/CSS3/Js
2. Background images and images used are embedded using unsplash API, <a href="https://source.unsplash.com/">read more</a> about unsplash API.
3. ionicons have been used to provide icon fonts, <a href="https://ionicons.com/">read more</a> about ionicons.
4. GoogleFonts have been used to make the typography beautiful and great, <a href="https://fonts.google.com/">read more</a> about GoogleFonts. 

#### 3Fs API
##### Installation

## Andela Uganda Cohort 12
3Fs project is a Challenge series requirement for **Cohort 12 Andela Uganda** Bootcampers\
1. Challenge 1 - Frontend (HTML/CSS) - Fast-Food-Fast Website
2. Challenge 2 - API Design - Fast-Food-Fast API 

### Contact information for thatGuy! our Awesome Developer!
- Name: **Sekabira Yasin** , call me *sekayasin*
- ping me: sekayasin@gmail.com
- I hang-out on GitHub, u can <a href="https://github.com/sekayasin">fork me</a> or on my tinkering <a href="https://sekayasin.me/">Portfolio</a>
- If u would like to follow me on Twitter, my username is *@sekayasin9*
