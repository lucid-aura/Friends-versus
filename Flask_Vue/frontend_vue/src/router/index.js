import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import FriendList from '../views/FriendList.vue'
import ChampionList from '../views/ChampionList.vue'
import ItemList from '../views/ItemList.vue'
import ChampionInfo from '../views/ChampionInfo.vue'
import PlayerInfo from '../views/PlayerInfo.vue'
import Login from '../views/Login.vue'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/riot/friendlist',
            name: 'friendList',
            component: FriendList,
        },
        {
            path: '/riot/itemlist',
            name: 'itemList',
            component: ItemList
        },
        {
            path: '/riot/championlist',
            name: 'championList',
            component: ChampionList,
        },
        {
            path: '/riot/championinfo',
            name: 'championInfo',
            component: ChampionInfo
        },
        {
            path: '/riot/playerinfo',
            name: 'playerinfo',
            component: PlayerInfo
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '*',
            redirect: '/'
        }
    ],
    linkActiveClass: 'active',
});
/*
VueRouter.beforeEach(to, from, next);

function hasQueryParams(route) {
  return !!Object.keys(route.query).length
}

function beforeEach(to, from, next) {
    if(!hasQueryParams(to) && hasQueryParams(from)){
        next({name: to.name, query: from.query});
    } else {
        next();
    }
}
*/