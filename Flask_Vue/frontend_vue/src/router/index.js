import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import FriendList from '../views/FriendList.vue'

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
            path: '*',
            redirect: '/'
        }
    ],
    linkActiveClass: 'active',
})