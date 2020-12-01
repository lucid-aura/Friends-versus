FROM node
WORKDIR /frontend_vue
ADD . ./
CMD rm package-lock.json && npm install && npm install cli && npm run serve
EXPOSE 8080