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


