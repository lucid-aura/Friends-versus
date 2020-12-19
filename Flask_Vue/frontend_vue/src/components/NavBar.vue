<template>
    <header class="masthead mb-auto site-header">
        <div class="inner">
            <nav class="nav nav-masthead justify-content-center">
                <router-link to="/" class="nav-link" exact>
                    Home
                </router-link>
                <router-link to="/riot/friendlist" class="nav-link" :disabled=!get_check_login() :event="get_check_login() ? 'click' : ''" exact>
                    Friend list
                </router-link>
                <router-link to="/riot/itemlist" class="nav-link" exact>
                    Items
                </router-link>
                <router-link to="/riot/championlist" class="nav-link" exact>
                    Champions
                </router-link>
                 <router-link to="/login" class="nav-link">
                    Login
                </router-link>
            </nav>

        </div>

    </header>
</template>

<script>
export default {
    name: 'NavBar',
    data() {
        return{
            check_login: false,
            user_name: ''
        }
    },
    methods: {
        get_check_login() {
            return this.check_login
        },
        need_login() {
            alert('로그인이 필요합니다.');
            if(this.$route.path !== '/') this.$router.push('/')
        },
        logout() {
            this.user_name = '';
            this.check_login = false;
            this.$root.$children[0].$children[1].login_id = ''; // login_id reset
            alert('로그아웃 되었습니다.');
            if(this.$route.path !== '/') this.$router.replace({path:'/'});
        }
    },
}
</script>