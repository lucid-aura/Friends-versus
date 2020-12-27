<template>
    <header class="masthead mb-auto site-header">
        <div class="inner">
            <nav class="nav nav-masthead justify-content-center">
                <router-link to="/" class="nav-link" exact>
                    <span type="button" @click="gohome"> Home </span>
                </router-link>
                <router-link to="/user/friendlist" class="nav-link" exact>
                    Friend list
                </router-link>
                <router-link to="/riot/itemlist" class="nav-link" exact>
                    Items
                </router-link>
                <router-link to="/riot/championlist" class="nav-link" exact>
                    Champions
                </router-link>
                 <router-link to="/login" class="nav-link" >
                    <span type="button" @click="logout" id="loginbtn" name="loginbtn"> {{ login }} </span>
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
            login: 'login'
        }
    },
    mounted: function() {
            this.$root.$on('login', (text) => { // here you need to use the arrow function
            console.log(text)
            this.login = text;
            console.log(this.login)
        });
    },
    methods: {
        get_check_login() {
            return this.check_login
        },
        need_login() {
            alert('로그인이 필요합니다.');
            if(this.$route.path !== '/') this.$router.push('/')
        },
        gohome() {
            this.$root.$emit('home', '');
        },
        logout() {
            if (this.login == 'logout'){
                this.login = 'login';
                sessionStorage.removeItem('jtw-token')
                alert('로그아웃 되었습니다.');
            }
        }
    },
}
</script>