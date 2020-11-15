import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import FriendList from '../views/FriendList.vue'
import ChampionList from '../views/ChampionList.vue'
import ItemList from '../views/ItemList.vue'
import ChampionInfo from '../views/ChampionInfo.vue'

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
            path: '/friendlist',
            name: 'friendList',
            component: FriendList
        },
        {
            path: '/itemlist',
            name: 'itemList',
            component: ItemList
        },
        {
            path: '/championlist',
            name: 'championList',
            component: ChampionList,
        },
        {
            path: '/championinfo',
            name: 'championInfo',
            component: ChampionInfo
        },

        {
            path: '*',
            redirect: '/'
        }
    ],
    linkActiveClass: 'active',
})