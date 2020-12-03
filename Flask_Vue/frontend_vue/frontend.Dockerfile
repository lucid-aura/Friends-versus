FROM node
WORKDIR /frontend_vue
COPY package*.json ./
ADD . ./
CMD rm package-lock.json && npm install && npm install cli && npm install axios && npm run serve
EXPOSE 8080