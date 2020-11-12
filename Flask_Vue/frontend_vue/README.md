# frontend_vue
## Customizing application
- src/App.vue : Component와 Routes에 포함하는 템플릿
- src/main.js : app 셋업과 main 임포트 수행
- src/router/index.js : app의 Routes 정의
- src/view/ : *.vue templates, view 표현
- src/components/ : *.vue.templates, views 내에서 재사용 가능
- src/assets/css/ : app 의 CSS
- public/index.html : app의 진입점
- p.s. src/plugins/ : *.js의 추가 플러그인

## main.js
- imports
- settings
- app mounting
블록을 가지고 있음
## public/index.html
???
`<div id="app"></div>`
???
## App.vue
기본 HTML과 비슷하다.
- template
- scripts(optional)
- styles(optional)
## route/index.js
routes와 Vue view들을 바인딩하는데 route/index.js를 사용한다.
## Home.vue
매우 기본적임, Base component 에 template와 script를 포함한다.
## FriendList.vue
이 애플리케이션의 함수 부분
## Vue template
입력이 리스트이고 루프는 v-for를 사용할 수 있다
``` v-for = "(item, index) in friend_list" ```
데이터 수정과 리스트 업데이트를 위해 v-model을 사용해서 리스트의 원소를 채워진 거에 바인딩한다.
``` v-model = "friend_list[index].nick_name" ```
이벤트는 @를 사용해서 정의되고 
``` @click = "addRow" ```
:를 property와 함께 사용하면 쌍따옴표 내의 변수를 사용할 수 있음
``` :key = "index" ```
v- 로 시작하는 태그는 Vue/Vuetify 래퍼의 축약 버전이다.

## Vue script


## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
