FROM node:alpine

WORKDIR /app

COPY package.json package.json

RUN npm i

COPY . .

CMD npm start

EXPOSE 3000